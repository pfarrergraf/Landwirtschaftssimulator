from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from landwirtschaftssimulator.domain import ExecutionMode, FieldStage, GameDate  # noqa: E402
from landwirtschaftssimulator.engine import SimulationEngine, SimulationError  # noqa: E402


class FieldStateMachineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = SimulationEngine.from_repo(ROOT)
        self.farm = self.engine.new_farm("Anna", "Sonnenhof")
        self.farm.date = GameDate(1, 9, 1)

    def test_complete_wheat_cycle(self) -> None:
        self.engine.prepare_field(self.farm, "field_01")
        self.engine.sow(self.farm, "field_01", "wheat")
        self.engine.fertilize(self.farm, "field_01")
        self.engine.advance_days(self.farm, 240)
        self.assertEqual(self.farm.fields["field_01"].stage, FieldStage.HARVEST_READY)
        tonnes = self.engine.harvest(self.farm, "field_01")
        self.assertGreater(tonnes, 0)
        revenue = self.engine.sell(self.farm, "wheat")
        self.assertGreater(revenue, 0)
        self.assertEqual(self.farm.fields["field_01"].stage, FieldStage.HARVESTED)

    def test_invalid_transition_does_not_charge_cash(self) -> None:
        cash = self.farm.cash_eur
        with self.assertRaises(SimulationError):
            self.engine.sow(self.farm, "field_01", "wheat")
        self.assertEqual(self.farm.cash_eur, cash)

    def test_special_crop_can_use_contractor(self) -> None:
        self.farm.date = GameDate(1, 3, 1)
        self.engine.prepare_field(self.farm, "field_03")
        self.engine.sow(self.farm, "field_03", "sugar_beet")
        self.engine.fertilize(self.farm, "field_03")
        self.engine.advance_days(self.farm, 120)
        tonnes = self.engine.harvest(
            self.farm,
            "field_03",
            mode=ExecutionMode.CONTRACTOR,
        )
        self.assertGreater(tonnes, 0)
        self.assertTrue(any(entry.category == "contractor" for entry in self.farm.ledger))


if __name__ == "__main__":
    unittest.main()
