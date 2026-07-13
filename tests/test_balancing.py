from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.balancer.simulate_year import simulate_crop  # noqa: E402
from tools.common import load_json  # noqa: E402


class BalancingTests(unittest.TestCase):
    def test_simulation_is_deterministic(self) -> None:
        wheat = load_json("data/crops/crops.json")["crops"][0]
        self.assertEqual(simulate_crop(wheat, 10, 2026), simulate_crop(wheat, 10, 2026))

    def test_all_crops_produce_finite_results(self) -> None:
        for crop in load_json("data/crops/crops.json")["crops"]:
            result = simulate_crop(crop, 10, 2026)
            self.assertIsInstance(result["profit"], int)
            self.assertGreater(result["revenue"], 0)
            self.assertGreater(result["cost"], 0)


if __name__ == "__main__":
    unittest.main()
