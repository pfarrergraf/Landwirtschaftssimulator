from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.common import load_json  # noqa: E402


def validate() -> list[str]:
    errors: list[str] = []
    start = load_json("data/game/start_state.json")
    fields = load_json("data/fields/fields.json")["fields"]
    crops = load_json("data/crops/crops.json")["crops"]
    machines = load_json("data/machines/machines.json")["machines"]
    levels = load_json("data/difficulty/levels.json")["levels"]

    if start["starting_cash_eur"] != 100000:
        errors.append("starting_cash_eur must be exactly 100000")
    if len(start["field_ids"]) != 10:
        errors.append("start state must contain exactly ten field ids")
    if len(fields) != 10:
        errors.append("field catalog must contain exactly ten fields")
    if sum(field["hectares"] for field in fields) != 60:
        errors.append("starter fields must total 60 hectares")

    machine_by_id = {machine["id"]: machine for machine in machines}
    owned_ids = start["owned_vehicle_ids"]
    if len(owned_ids) != 4:
        errors.append("start state must contain exactly four owned vehicles")
    missing = [item for item in owned_ids if item not in machine_by_id]
    if missing:
        errors.append(f"unknown starter machine ids: {missing}")
    else:
        categories = Counter(machine_by_id[item]["category"] for item in owned_ids)
        expected = Counter({"tractor": 1, "trailer": 2, "grain_combine": 1})
        if categories != expected:
            errors.append(f"starter categories must be {dict(expected)}, got {dict(categories)}")

    all_ids = [field["id"] for field in fields] + [crop["id"] for crop in crops] + [machine["id"] for machine in machines]
    duplicates = [item for item, count in Counter(all_ids).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate ids: {duplicates}")

    for machine in machines:
        if machine["brand"] != "Neutral":
            if not machine.get("license_status"):
                errors.append(f"machine {machine['id']} lacks license_status")
            if not machine.get("asset_status"):
                errors.append(f"machine {machine['id']} lacks asset_status")

    required_levels = {"easy", "primary_school", "medium", "professional"}
    actual_levels = {level["id"] for level in levels}
    if actual_levels != required_levels:
        errors.append(f"difficulty levels must be {sorted(required_levels)}")

    for crop in crops:
        for key in ("seed_cost_eur_per_ha", "care_cost_eur_per_ha", "yield_t_per_ha", "normal_price_eur_per_t"):
            if crop.get(key, 0) <= 0:
                errors.append(f"crop {crop['id']} has invalid {key}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Data validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Data validation passed: starter invariants, catalogs and brand metadata are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
