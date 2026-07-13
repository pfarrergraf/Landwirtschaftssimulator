from __future__ import annotations

import hashlib
import random
from pathlib import Path
from typing import Any

from .catalog import Catalog
from .domain import ExecutionMode, FarmState, FieldStage, FieldState, GameDate, MachineState


class SimulationError(RuntimeError):
    """Raised for invalid game actions that must not mutate the farm state."""


SOIL_YIELD_FACTORS = {
    "good": 1.05,
    "medium": 1.0,
    "heavy": 0.98,
    "sandy": 0.92,
    "clay": 0.96,
    "weak": 0.86,
}

CATEGORY_WORK_RATE_HA_PER_HOUR = {
    "tractor": 2.2,
    "grain_combine": 3.0,
    "beet_harvester": 1.4,
    "potato_harvester": 1.2,
    "forage_harvester": 2.4,
}

CATEGORY_WEAR_PER_HOUR = {
    "tractor": 0.0025,
    "grain_combine": 0.004,
    "beet_harvester": 0.0045,
    "potato_harvester": 0.0045,
    "forage_harvester": 0.004,
}

OPERATION_MACHINE_CATEGORY = {
    "prepare": "tractor",
    "sow": "tractor",
    "fertilize": "tractor",
    "harvest_grain": "grain_combine",
    "harvest_beet": "beet_harvester",
    "harvest_potato": "potato_harvester",
}

OPERATION_CONTRACTOR_KEY = {
    "prepare": "plough",
    "sow": "sow",
    "fertilize": "sow",
    "harvest_grain": "grain_harvest",
    "harvest_beet": "beet_harvest",
    "harvest_potato": "potato_harvest",
}


class SimulationEngine:
    def __init__(self, catalog: Catalog):
        self.catalog = catalog

    @classmethod
    def from_repo(cls, repo_root: Path) -> SimulationEngine:
        return cls(Catalog.load(repo_root))

    def new_farm(
        self,
        profile_name: str,
        farm_name: str,
        difficulty: str = "primary_school",
        seed: int = 2026,
    ) -> FarmState:
        start = self.catalog.start
        fields = {
            field_id: FieldState(
                id=field_id,
                hectares=float(self.catalog.fields[field_id]["hectares"]),
                soil=self.catalog.fields[field_id]["soil"],
                suitability=list(self.catalog.fields[field_id]["suitability"]),
            )
            for field_id in start["field_ids"]
        }
        machines = {
            machine_id: self._machine_state(machine_id, owned=True)
            for machine_id in start["owned_vehicle_ids"]
        }
        return FarmState(
            profile_name=profile_name,
            farm_name=farm_name,
            difficulty=difficulty,
            seed=seed,
            date=GameDate(year=1, month=1, day=1),
            cash_eur=int(start["starting_cash_eur"]),
            fields=fields,
            machines=machines,
        )

    def advance_days(self, farm: FarmState, days: int) -> None:
        if days < 0:
            raise SimulationError("cannot move time backwards")
        old_ordinal = farm.date.ordinal
        farm.date = farm.date.add_days(days)
        elapsed = farm.date.ordinal - old_ordinal
        for field in farm.fields.values():
            if field.stage in {FieldStage.SOWN, FieldStage.GROWING}:
                field.growth_days += elapsed
                if field.growth_days > 0:
                    field.stage = FieldStage.GROWING
                crop = self.catalog.crops[field.crop_id or ""]
                if field.growth_days >= self._required_growth_days(crop):
                    field.stage = FieldStage.HARVEST_READY
        self._expire_rentals(farm)

    def prepare_field(
        self,
        farm: FarmState,
        field_id: str,
        mode: ExecutionMode = ExecutionMode.OWNED,
        machine_id: str | None = None,
    ) -> None:
        field = self._field(farm, field_id)
        if field.stage not in {FieldStage.FALLOW, FieldStage.HARVESTED}:
            raise SimulationError(f"field {field_id} cannot be prepared from stage {field.stage}")
        self._assert_affordable(
            farm,
            self._operation_cash_cost(field, "prepare", mode),
            f"Feldvorbereitung {field_id}",
        )
        self._charge_operation(farm, field, "prepare", mode, machine_id)
        field.stage = FieldStage.PREPARED
        field.prepared = True
        field.crop_id = None
        field.fertilized = False
        field.sown_on = None
        field.growth_days = 0

    def sow(
        self,
        farm: FarmState,
        field_id: str,
        crop_id: str,
        mode: ExecutionMode = ExecutionMode.OWNED,
        machine_id: str | None = None,
    ) -> None:
        field = self._field(farm, field_id)
        crop = self._crop(crop_id)
        if field.stage != FieldStage.PREPARED:
            raise SimulationError(f"field {field_id} must be prepared before sowing")
        if not self._sowing_window_open(crop, farm.date.month):
            raise SimulationError(f"{crop_id} cannot be sown in month {farm.date.month}")
        seed_cost = round(field.hectares * crop["seed_cost_eur_per_ha"])
        self._assert_affordable(
            farm,
            self._operation_cash_cost(field, "sow", mode) + seed_cost,
            f"Aussaat {crop_id} auf {field_id}",
        )
        self._charge_operation(farm, field, "sow", mode, machine_id)
        farm.post(-seed_cost, "seed", f"Saatgut {crop_id} auf {field_id}")
        field.stage = FieldStage.SOWN
        field.crop_id = crop_id
        field.sown_on = farm.date
        field.growth_days = 0

    def fertilize(
        self,
        farm: FarmState,
        field_id: str,
        mode: ExecutionMode = ExecutionMode.OWNED,
        machine_id: str | None = None,
    ) -> None:
        field = self._field(farm, field_id)
        if field.stage not in {FieldStage.SOWN, FieldStage.GROWING}:
            raise SimulationError(f"field {field_id} cannot be fertilized at stage {field.stage}")
        if field.fertilized:
            raise SimulationError(f"field {field_id} is already fertilized")
        crop = self._crop(field.crop_id or "")
        care_cost = round(field.hectares * crop["care_cost_eur_per_ha"])
        self._assert_affordable(
            farm,
            self._operation_cash_cost(field, "fertilize", mode) + care_cost,
            f"Pflege {field.crop_id} auf {field_id}",
        )
        self._charge_operation(farm, field, "fertilize", mode, machine_id)
        farm.post(-care_cost, "crop_care", f"Pflege {field.crop_id} auf {field_id}")
        field.fertilized = True

    def harvest(
        self,
        farm: FarmState,
        field_id: str,
        mode: ExecutionMode = ExecutionMode.OWNED,
        machine_id: str | None = None,
    ) -> float:
        field = self._field(farm, field_id)
        if field.stage != FieldStage.HARVEST_READY:
            raise SimulationError(f"field {field_id} is not harvest-ready")
        crop = self._crop(field.crop_id or "")
        operation = self._harvest_operation(crop["harvest_category"])
        self._assert_affordable(
            farm,
            self._operation_cash_cost(field, operation, mode),
            f"Ernte {field.crop_id} auf {field_id}",
        )
        self._charge_operation(farm, field, operation, mode, machine_id)
        weather = self._factor(farm, field.id, "weather", 0.85, 1.12)
        suitability = 1.0 if field.crop_id in field.suitability else 0.88
        fertilizer = 1.05 if field.fertilized else 0.82
        soil = SOIL_YIELD_FACTORS.get(field.soil, 1.0)
        tonnes = (
            field.hectares
            * crop["yield_t_per_ha"]
            * weather
            * suitability
            * fertilizer
            * soil
        )
        tonnes = round(tonnes, 3)
        farm.inventory_t[field.crop_id or ""] = farm.inventory_t.get(field.crop_id or "", 0.0) + tonnes
        field.last_yield_t = tonnes
        field.stage = FieldStage.HARVESTED
        return tonnes

    def sell(self, farm: FarmState, crop_id: str, tonnes: float | None = None) -> int:
        crop = self._crop(crop_id)
        available = farm.inventory_t.get(crop_id, 0.0)
        quantity = available if tonnes is None else tonnes
        if quantity <= 0 or quantity > available + 1e-9:
            raise SimulationError(f"invalid sale quantity {quantity} for inventory {available}")
        market = self._factor(farm, crop_id, "market", 0.88, 1.15)
        revenue = round(quantity * crop["normal_price_eur_per_t"] * market)
        farm.inventory_t[crop_id] = round(available - quantity, 5)
        farm.post(revenue, "crop_sale", f"Verkauf {quantity:.3f} t {crop_id}")
        return revenue

    def buy_machine(self, farm: FarmState, machine_id: str) -> MachineState:
        if machine_id in farm.machines and farm.machines[machine_id].owned:
            raise SimulationError(f"machine {machine_id} is already owned")
        catalog_item = self._machine(machine_id)
        price = int(catalog_item["game_price_eur"])
        if price <= 0:
            raise SimulationError(f"machine {machine_id} is not offered for purchase")
        try:
            farm.post(-price, "machine_purchase", f"Kauf {machine_id}")
        except ValueError as exc:
            raise SimulationError(str(exc)) from exc
        state = self._machine_state(machine_id, owned=True)
        farm.machines[machine_id] = state
        return state

    def rent_machine(self, farm: FarmState, machine_id: str, days: int = 1) -> MachineState:
        if days < 1:
            raise SimulationError("rental days must be >= 1")
        item = self._machine(machine_id)
        daily = int(item.get("rental_eur_per_day") or self.catalog.economy["rental_base_eur_per_day"].get(item["category"], 0))
        if daily <= 0:
            raise SimulationError(f"machine {machine_id} has no rental tariff")
        total = daily * days
        try:
            farm.post(-total, "machine_rental", f"Miete {machine_id} fuer {days} Tag(e)")
        except ValueError as exc:
            raise SimulationError(str(exc)) from exc
        state = self._machine_state(machine_id, owned=False)
        state.rented_until = farm.date.add_days(days - 1)
        farm.machines[machine_id] = state
        return state

    def repair_machine(self, farm: FarmState, machine_id: str) -> int:
        machine = self._available_machine(farm, machine_id)
        if not machine.owned:
            raise SimulationError("rented machines cannot be repaired by the player")
        if machine.wear <= 0:
            return 0
        repair_cost = max(500, round(machine.purchase_price_eur * machine.wear * 0.04))
        try:
            farm.post(-repair_cost, "machine_repair", f"Reparatur {machine_id}")
        except ValueError as exc:
            raise SimulationError(str(exc)) from exc
        machine.wear = max(0.0, machine.wear - 0.65)
        machine.repair_count += 1
        return repair_cost

    def charge_annual_maintenance(self, farm: FarmState) -> int:
        total = 0
        for machine in farm.machines.values():
            if not machine.owned:
                continue
            if machine.category == "tractor":
                cost = int(self.catalog.economy["tractor_fixed_annual_maintenance_eur"])
            elif machine.category == "grain_combine":
                cost = int(self.catalog.economy["grain_combine_fixed_annual_maintenance_eur"])
            else:
                cost = max(250, round(machine.purchase_price_eur * 0.008))
            total += cost
        try:
            farm.post(-total, "annual_maintenance", "Jaehrliche Maschinenwartung")
        except ValueError as exc:
            raise SimulationError(str(exc)) from exc
        return total

    def _operation_cash_cost(
        self,
        field: FieldState,
        operation: str,
        mode: ExecutionMode,
    ) -> int:
        required_category = OPERATION_MACHINE_CATEGORY[operation]
        if mode == ExecutionMode.CONTRACTOR:
            key = OPERATION_CONTRACTOR_KEY[operation]
            return round(
                field.hectares * int(self.catalog.economy["contractor_eur_per_ha"][key])
            )
        fuel_l_per_ha = 12.0 if required_category == "tractor" else 24.0
        return round(
            field.hectares
            * fuel_l_per_ha
            * float(self.catalog.economy["fuel_price_eur_per_l"])
        )

    @staticmethod
    def _assert_affordable(farm: FarmState, amount_eur: int, description: str) -> None:
        if amount_eur < 0:
            raise SimulationError("cost must not be negative")
        if farm.cash_eur < amount_eur:
            raise SimulationError(
                f"insufficient cash for {description}: {farm.cash_eur} EUR available, "
                f"{amount_eur} EUR required"
            )

    def _charge_operation(
        self,
        farm: FarmState,
        field: FieldState,
        operation: str,
        mode: ExecutionMode,
        machine_id: str | None,
    ) -> None:
        required_category = OPERATION_MACHINE_CATEGORY[operation]
        if mode == ExecutionMode.CONTRACTOR:
            key = OPERATION_CONTRACTOR_KEY[operation]
            price_per_ha = int(self.catalog.economy["contractor_eur_per_ha"][key])
            cost = round(field.hectares * price_per_ha)
            try:
                farm.post(-cost, "contractor", f"Lohnunternehmen {operation} auf {field.id}")
            except ValueError as exc:
                raise SimulationError(str(exc)) from exc
            return

        machine = self._select_machine(farm, required_category, machine_id)
        if machine.wear >= 1.0:
            raise SimulationError(f"machine {machine.id} requires repair before further use")
        if mode == ExecutionMode.RENTED and machine.owned:
            raise SimulationError(f"machine {machine.id} is owned, not rented")
        if mode == ExecutionMode.OWNED and not machine.owned:
            raise SimulationError(f"machine {machine.id} is rented, not owned")
        rate = CATEGORY_WORK_RATE_HA_PER_HOUR.get(required_category, 2.0)
        hours = field.hectares / rate
        wear = hours * CATEGORY_WEAR_PER_HOUR.get(required_category, 0.002)
        machine.operating_hours += hours
        machine.wear = min(1.5, machine.wear + wear)
        fuel_l_per_ha = 12.0 if required_category == "tractor" else 24.0
        fuel_cost = round(field.hectares * fuel_l_per_ha * self.catalog.economy["fuel_price_eur_per_l"])
        try:
            farm.post(-fuel_cost, "fuel", f"Kraftstoff {operation} auf {field.id}")
        except ValueError as exc:
            raise SimulationError(str(exc)) from exc

    def _select_machine(
        self,
        farm: FarmState,
        category: str,
        machine_id: str | None,
    ) -> MachineState:
        if machine_id:
            machine = self._available_machine(farm, machine_id)
            if machine.category != category:
                raise SimulationError(
                    f"machine {machine_id} has category {machine.category}, expected {category}"
                )
            return machine
        candidates = [
            machine
            for machine in farm.machines.values()
            if machine.category == category and self._is_available_on(machine, farm.date)
        ]
        if not candidates:
            raise SimulationError(f"no available machine in category {category}")
        return sorted(candidates, key=lambda item: (not item.owned, item.wear, item.id))[0]

    def _available_machine(self, farm: FarmState, machine_id: str) -> MachineState:
        if machine_id not in farm.machines:
            raise SimulationError(f"machine {machine_id} is not in the farm fleet")
        machine = farm.machines[machine_id]
        if not self._is_available_on(machine, farm.date):
            raise SimulationError(f"machine {machine_id} is not currently available")
        return machine

    @staticmethod
    def _is_available_on(machine: MachineState, date: GameDate) -> bool:
        return machine.owned or (machine.rented_until is not None and machine.rented_until >= date)

    def _expire_rentals(self, farm: FarmState) -> None:
        expired = [
            machine_id
            for machine_id, machine in farm.machines.items()
            if not machine.owned and not self._is_available_on(machine, farm.date)
        ]
        for machine_id in expired:
            del farm.machines[machine_id]

    def _field(self, farm: FarmState, field_id: str) -> FieldState:
        try:
            return farm.fields[field_id]
        except KeyError as exc:
            raise SimulationError(f"unknown field {field_id}") from exc

    def _crop(self, crop_id: str) -> dict[str, Any]:
        try:
            return self.catalog.crops[crop_id]
        except KeyError as exc:
            raise SimulationError(f"unknown crop {crop_id}") from exc

    def _machine(self, machine_id: str) -> dict[str, Any]:
        try:
            return self.catalog.machines[machine_id]
        except KeyError as exc:
            raise SimulationError(f"unknown machine {machine_id}") from exc

    def _machine_state(self, machine_id: str, owned: bool) -> MachineState:
        item = self._machine(machine_id)
        return MachineState(
            id=machine_id,
            category=item["category"],
            condition=item["condition"],
            purchase_price_eur=int(item["game_price_eur"]),
            owned=owned,
            wear=0.18 if item["condition"] == "used" else 0.02,
        )

    @staticmethod
    def _required_growth_days(crop: dict[str, Any]) -> int:
        return 240 if crop["season"] == "autumn_sown" else 120

    @staticmethod
    def _sowing_window_open(crop: dict[str, Any], month: int) -> bool:
        if crop["season"] == "autumn_sown":
            return month in {9, 10, 11}
        return month in {3, 4, 5}

    @staticmethod
    def _harvest_operation(category: str) -> str:
        if category == "grain_combine":
            return "harvest_grain"
        if category == "beet_harvester":
            return "harvest_beet"
        if category == "potato_harvester":
            return "harvest_potato"
        raise SimulationError(f"unsupported harvest category {category}")

    @staticmethod
    def _factor(farm: FarmState, subject: str, kind: str, lower: float, upper: float) -> float:
        key = f"{farm.seed}:{farm.date.year}:{subject}:{kind}".encode("utf-8")
        digest = hashlib.sha256(key).hexdigest()
        rng = random.Random(int(digest[:16], 16))
        return round(rng.uniform(lower, upper), 5)
