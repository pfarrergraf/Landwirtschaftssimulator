from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from landwirtschaftssimulator.domain import ExecutionMode, GameDate  # noqa: E402
from landwirtschaftssimulator.engine import SimulationEngine, SimulationError  # noqa: E402


class ProcurementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = SimulationEngine.from_repo(ROOT)
        self.farm = self.engine.new_farm("Ben", "Lindenhof")

    def test_purchase_requires_sufficient_cash(self) -> None:
        with self.assertRaises(SimulationError):
            self.engine.buy_machine(self.farm, "john_deere_6r_new")
        self.assertNotIn("john_deere_6r_new", self.farm.machines)

    def test_rental_expires(self) -> None:
        self.farm.date = GameDate(1, 3, 1)
        machine = self.engine.rent_machine(
            self.farm,
            "generic_beet_harvester_rental",
            days=2,
        )
        self.assertFalse(machine.owned)
        self.assertIn(machine.id, self.farm.machines)
        self.engine.advance_days(self.farm, 2)
        self.assertNotIn(machine.id, self.farm.machines)

    def test_machine_use_creates_wear_and_repair_cost(self) -> None:
        self.farm.date = GameDate(1, 9, 1)
        tractor = self.farm.machines["fendt_724_vario_used"]
        initial_wear = tractor.wear
        self.engine.prepare_field(
            self.farm,
            "field_05",
            mode=ExecutionMode.OWNED,
            machine_id=tractor.id,
        )
        self.assertGreater(tractor.wear, initial_wear)
        before = self.farm.cash_eur
        cost = self.engine.repair_machine(self.farm, tractor.id)
        self.assertGreater(cost, 0)
        self.assertEqual(self.farm.cash_eur, before - cost)


if __name__ == "__main__":
    unittest.main()
