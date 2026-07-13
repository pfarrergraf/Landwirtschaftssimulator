from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from .domain import ExecutionMode, GameDate
from .engine import SimulationEngine


@dataclass(frozen=True)
class RegressionSummary:
    years: int
    ending_cash_eur: int
    total_revenue_eur: int
    total_expenses_eur: int
    total_harvest_t: float
    digest: str


def run_economic_years(repo_root: Path, years: int = 100, seed: int = 2026) -> RegressionSummary:
    """Run a deterministic full-farm grain rotation for regression testing.

    The scenario uses all inherited fields and the owned tractor/combine. It is not a
    forecast; it is a stable integration scenario covering time, field transitions,
    costs, market prices, maintenance, wear and repairs.
    """
    if years < 1:
        raise ValueError("years must be >= 1")
    engine = SimulationEngine.from_repo(repo_root)
    farm = engine.new_farm("Regression", "Testhof", seed=seed)
    grain_crops = ("wheat", "barley", "rapeseed")
    total_harvest = 0.0

    for year in range(1, years + 1):
        farm.date = GameDate(year=year, month=9, day=1)
        planned: dict[str, str] = {}
        for index, field in enumerate(farm.fields.values()):
            suitable_grains = [crop for crop in grain_crops if crop in field.suitability]
            candidates = suitable_grains or ["wheat"]
            crop_id = candidates[(year + index - 1) % len(candidates)]
            planned[field.id] = crop_id
            engine.prepare_field(farm, field.id, ExecutionMode.OWNED)
            engine.sow(farm, field.id, crop_id, ExecutionMode.OWNED)
            engine.fertilize(farm, field.id, ExecutionMode.OWNED)

        engine.advance_days(farm, 240)
        for field_id, crop_id in planned.items():
            total_harvest += engine.harvest(farm, field_id, ExecutionMode.OWNED)
            engine.sell(farm, crop_id)

        engine.charge_annual_maintenance(farm)
        for machine in list(farm.machines.values()):
            if machine.owned and machine.wear >= 0.75:
                engine.repair_machine(farm, machine.id)

    revenue = sum(entry.amount_eur for entry in farm.ledger if entry.amount_eur > 0)
    expenses = -sum(entry.amount_eur for entry in farm.ledger if entry.amount_eur < 0)
    digest_payload = {
        "years": years,
        "seed": seed,
        "ending_cash_eur": farm.cash_eur,
        "total_revenue_eur": revenue,
        "total_expenses_eur": expenses,
        "total_harvest_t": round(total_harvest, 3),
        "ledger_entries": len(farm.ledger),
        "machine_hours": {
            key: round(machine.operating_hours, 3)
            for key, machine in sorted(farm.machines.items())
        },
        "repair_counts": {
            key: machine.repair_count for key, machine in sorted(farm.machines.items())
        },
    }
    digest = hashlib.sha256(
        json.dumps(digest_payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return RegressionSummary(
        years=years,
        ending_cash_eur=farm.cash_eur,
        total_revenue_eur=revenue,
        total_expenses_eur=expenses,
        total_harvest_t=round(total_harvest, 3),
        digest=digest,
    )
