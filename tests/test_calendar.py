from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from landwirtschaftssimulator.domain import GameDate, Season  # noqa: E402


class CalendarTests(unittest.TestCase):
    def test_seasons(self) -> None:
        self.assertEqual(GameDate(1, 1, 1).season, Season.WINTER)
        self.assertEqual(GameDate(1, 4, 1).season, Season.SPRING)
        self.assertEqual(GameDate(1, 7, 1).season, Season.SUMMER)
        self.assertEqual(GameDate(1, 10, 1).season, Season.AUTUMN)

    def test_360_day_calendar_rollover(self) -> None:
        self.assertEqual(GameDate(1, 12, 30).add_days(1), GameDate(2, 1, 1))
        self.assertEqual(GameDate(3, 1, 1).add_days(359), GameDate(3, 12, 30))


if __name__ == "__main__":
    unittest.main()
