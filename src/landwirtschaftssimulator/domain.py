from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from typing import Any


class Season(StrEnum):
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"


class FieldStage(StrEnum):
    FALLOW = "fallow"
    PREPARED = "prepared"
    SOWN = "sown"
    GROWING = "growing"
    HARVEST_READY = "harvest_ready"
    HARVESTED = "harvested"


class ExecutionMode(StrEnum):
    OWNED = "owned"
    RENTED = "rented"
    CONTRACTOR = "contractor"


@dataclass(frozen=True, order=True)
class GameDate:
    year: int = 1
    month: int = 1
    day: int = 1

    def __post_init__(self) -> None:
        if self.year < 1:
            raise ValueError("year must be >= 1")
        if not 1 <= self.month <= 12:
            raise ValueError("month must be between 1 and 12")
        if not 1 <= self.day <= 30:
            raise ValueError("day must be between 1 and 30")

    @property
    def season(self) -> Season:
        if self.month in {12, 1, 2}:
            return Season.WINTER
        if self.month in {3, 4, 5}:
            return Season.SPRING
        if self.month in {6, 7, 8}:
            return Season.SUMMER
        return Season.AUTUMN

    @property
    def ordinal(self) -> int:
        return (self.year - 1) * 360 + (self.month - 1) * 30 + self.day

    def add_days(self, days: int) -> GameDate:
        if days < 0:
            raise ValueError("days must be >= 0")
        zero_based = self.ordinal - 1 + days
        year, day_of_year = divmod(zero_based, 360)
        month, day = divmod(day_of_year, 30)
        return GameDate(year=year + 1, month=month + 1, day=day + 1)


@dataclass
class LedgerEntry:
    date: GameDate
    category: str
    amount_eur: int
    description: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "date": asdict(self.date),
            "category": self.category,
            "amount_eur": self.amount_eur,
            "description": self.description,
        }


@dataclass
class FieldState:
    id: str
    hectares: float
    soil: str
    suitability: list[str]
    stage: FieldStage = FieldStage.FALLOW
    crop_id: str | None = None
    prepared: bool = False
    fertilized: bool = False
    sown_on: GameDate | None = None
    growth_days: int = 0
    last_yield_t: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "hectares": self.hectares,
            "soil": self.soil,
            "suitability": list(self.suitability),
            "stage": self.stage.value,
            "crop_id": self.crop_id,
            "prepared": self.prepared,
            "fertilized": self.fertilized,
            "sown_on": asdict(self.sown_on) if self.sown_on else None,
            "growth_days": self.growth_days,
            "last_yield_t": self.last_yield_t,
        }


@dataclass
class MachineState:
    id: str
    category: str
    condition: str
    purchase_price_eur: int
    owned: bool = True
    rented_until: GameDate | None = None
    operating_hours: float = 0.0
    wear: float = 0.0
    repair_count: int = 0

    @property
    def available(self) -> bool:
        return self.owned or self.rented_until is not None

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "category": self.category,
            "condition": self.condition,
            "purchase_price_eur": self.purchase_price_eur,
            "owned": self.owned,
            "rented_until": asdict(self.rented_until) if self.rented_until else None,
            "operating_hours": round(self.operating_hours, 3),
            "wear": round(self.wear, 5),
            "repair_count": self.repair_count,
        }


@dataclass
class FarmState:
    profile_name: str
    farm_name: str
    difficulty: str
    seed: int
    date: GameDate
    cash_eur: int
    fields: dict[str, FieldState] = field(default_factory=dict)
    machines: dict[str, MachineState] = field(default_factory=dict)
    inventory_t: dict[str, float] = field(default_factory=dict)
    ledger: list[LedgerEntry] = field(default_factory=list)

    def post(self, amount_eur: int, category: str, description: str) -> None:
        next_cash = self.cash_eur + amount_eur
        if next_cash < 0:
            raise ValueError(
                f"insufficient cash for {description}: {self.cash_eur} EUR available, "
                f"{-amount_eur} EUR required"
            )
        self.cash_eur = next_cash
        self.ledger.append(
            LedgerEntry(
                date=self.date,
                category=category,
                amount_eur=amount_eur,
                description=description,
            )
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "profile_name": self.profile_name,
            "farm_name": self.farm_name,
            "difficulty": self.difficulty,
            "seed": self.seed,
            "date": asdict(self.date),
            "cash_eur": self.cash_eur,
            "fields": {key: value.to_dict() for key, value in sorted(self.fields.items())},
            "machines": {key: value.to_dict() for key, value in sorted(self.machines.items())},
            "inventory_t": {key: round(value, 5) for key, value in sorted(self.inventory_t.items())},
            "ledger": [entry.to_dict() for entry in self.ledger],
        }
