from __future__ import annotations

import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.common import load_json  # noqa: E402
from tools.validator.validate_data import validate  # noqa: E402


class DataInvariantTests(unittest.TestCase):
    def test_full_validation(self) -> None:
        self.assertEqual(validate(), [])

    def test_starter_package(self) -> None:
        start = load_json("data/game/start_state.json")
        machines = load_json("data/machines/machines.json")["machines"]
        machine_by_id = {item["id"]: item for item in machines}
        categories = Counter(machine_by_id[item]["category"] for item in start["owned_vehicle_ids"])
        self.assertEqual(start["starting_cash_eur"], 100000)
        self.assertEqual(len(start["field_ids"]), 10)
        self.assertEqual(categories, Counter({"tractor": 1, "trailer": 2, "grain_combine": 1}))

    def test_real_brands_have_license_metadata(self) -> None:
        machines = load_json("data/machines/machines.json")["machines"]
        for machine in machines:
            if machine["brand"] != "Neutral":
                self.assertIn(machine["license_status"], {"planned", "contact_requested", "pending", "licensed", "rejected", "fictional_replacement"})
                self.assertTrue(machine["asset_status"])


if __name__ == "__main__":
    unittest.main()
