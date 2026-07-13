from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from landwirtschaftssimulator.regression import run_economic_years  # noqa: E402


class HundredYearRegressionTests(unittest.TestCase):
    def test_hundred_years_are_deterministic_and_solvent(self) -> None:
        first = run_economic_years(ROOT, years=100, seed=2026)
        second = run_economic_years(ROOT, years=100, seed=2026)
        self.assertEqual(first, second)
        self.assertGreater(first.ending_cash_eur, 0)
        self.assertGreater(first.total_harvest_t, 0)
        self.assertEqual(len(first.digest), 64)

    def test_seed_changes_digest(self) -> None:
        first = run_economic_years(ROOT, years=10, seed=1)
        second = run_economic_years(ROOT, years=10, seed=2)
        self.assertNotEqual(first.digest, second.digest)


if __name__ == "__main__":
    unittest.main()
