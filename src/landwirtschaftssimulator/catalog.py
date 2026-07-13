from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Catalog:
    root: Path
    start: dict[str, Any]
    fields: dict[str, dict[str, Any]]
    crops: dict[str, dict[str, Any]]
    machines: dict[str, dict[str, Any]]
    implements: dict[str, dict[str, Any]]
    economy: dict[str, Any]

    @classmethod
    def load(cls, root: Path) -> Catalog:
        def read(relative: str) -> dict[str, Any]:
            with (root / relative).open("r", encoding="utf-8") as handle:
                return json.load(handle)

        fields = read("data/fields/fields.json")["fields"]
        crops = read("data/crops/crops.json")["crops"]
        machines = read("data/machines/machines.json")["machines"]
        implements = read("data/machines/implements.json")["implements"]
        return cls(
            root=root,
            start=read("data/game/start_state.json"),
            fields={item["id"]: item for item in fields},
            crops={item["id"]: item for item in crops},
            machines={item["id"]: item for item in machines},
            implements={item["id"]: item for item in implements},
            economy=read("data/economy/economy.json"),
        )
