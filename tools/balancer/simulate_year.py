from __future__ import annotations

import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.common import load_json  # noqa: E402


def simulate_crop(crop: dict, hectares: float, seed: int = 2026) -> dict:
    rng = random.Random(f"{seed}:{crop['id']}")
    weather_factor = round(rng.uniform(0.85, 1.12), 3)
    market_factor = round(rng.uniform(0.88, 1.15), 3)
    variable_cost = hectares * (crop["seed_cost_eur_per_ha"] + crop["care_cost_eur_per_ha"])
    harvest_cost_per_ha = 120 if crop["harvest_category"] == "grain_combine" else 420
    harvest_cost = hectares * harvest_cost_per_ha
    tonnes = hectares * crop["yield_t_per_ha"] * weather_factor
    revenue = tonnes * crop["normal_price_eur_per_t"] * market_factor
    profit = revenue - variable_cost - harvest_cost
    return {
        "crop": crop["name_de"],
        "hectares": hectares,
        "weather_factor": weather_factor,
        "market_factor": market_factor,
        "revenue": round(revenue),
        "cost": round(variable_cost + harvest_cost),
        "profit": round(profit),
    }


def main() -> int:
    crops = load_json("data/crops/crops.json")["crops"]
    print("Deterministic 10 ha comparison (seed 2026)")
    print("-" * 72)
    for crop in crops:
        result = simulate_crop(crop, hectares=10, seed=2026)
        print(
            f"{result['crop']:<16} revenue={result['revenue']:>7} EUR "
            f"cost={result['cost']:>7} EUR profit={result['profit']:>7} EUR"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
