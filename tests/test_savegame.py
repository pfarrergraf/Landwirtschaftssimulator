from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from landwirtschaftssimulator.domain import GameDate  # noqa: E402
from landwirtschaftssimulator.engine import SimulationEngine  # noqa: E402
from landwirtschaftssimulator.persistence import SavegameError, load_savegame, save_savegame  # noqa: E402


class SavegameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = SimulationEngine.from_repo(ROOT)

    def test_roundtrip_is_lossless(self) -> None:
        farm = self.engine.new_farm("Mia", "Hof am Bach", seed=77)
        farm.date = GameDate(2, 9, 1)
        self.engine.prepare_field(farm, "field_01")
        self.engine.sow(farm, "field_01", "wheat")
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "save.json"
            save_savegame(farm, path)
            loaded = load_savegame(path)
        self.assertEqual(loaded.to_dict(), farm.to_dict())

    def test_unknown_schema_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "save.json"
            path.write_text(json.dumps({"schema_version": 99, "game": {}}), encoding="utf-8")
            with self.assertRaises(SavegameError):
                load_savegame(path)


if __name__ == "__main__":
    unittest.main()
