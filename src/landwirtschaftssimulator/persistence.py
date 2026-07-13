from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .domain import FarmState, FieldStage, FieldState, GameDate, LedgerEntry, MachineState

SAVEGAME_SCHEMA_VERSION = 1


class SavegameError(ValueError):
    pass


def save_savegame(farm: FarmState, path: Path) -> None:
    payload = {
        "schema_version": SAVEGAME_SCHEMA_VERSION,
        "game": farm.to_dict(),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def load_savegame(path: Path) -> FarmState:
    try:
        payload: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SavegameError(f"cannot read savegame {path}: {exc}") from exc
    if payload.get("schema_version") != SAVEGAME_SCHEMA_VERSION:
        raise SavegameError(
            f"unsupported savegame schema {payload.get('schema_version')}; "
            f"expected {SAVEGAME_SCHEMA_VERSION}"
        )
    game = payload.get("game")
    if not isinstance(game, dict):
        raise SavegameError("savegame has no game object")
    try:
        date = GameDate(**game["date"])
        fields = {
            field_id: FieldState(
                id=item["id"],
                hectares=float(item["hectares"]),
                soil=item["soil"],
                suitability=list(item["suitability"]),
                stage=FieldStage(item["stage"]),
                crop_id=item.get("crop_id"),
                prepared=bool(item.get("prepared", False)),
                fertilized=bool(item.get("fertilized", False)),
                sown_on=GameDate(**item["sown_on"]) if item.get("sown_on") else None,
                growth_days=int(item.get("growth_days", 0)),
                last_yield_t=float(item.get("last_yield_t", 0.0)),
            )
            for field_id, item in game["fields"].items()
        }
        machines = {
            machine_id: MachineState(
                id=item["id"],
                category=item["category"],
                condition=item["condition"],
                purchase_price_eur=int(item["purchase_price_eur"]),
                owned=bool(item["owned"]),
                rented_until=GameDate(**item["rented_until"]) if item.get("rented_until") else None,
                operating_hours=float(item.get("operating_hours", 0.0)),
                wear=float(item.get("wear", 0.0)),
                repair_count=int(item.get("repair_count", 0)),
            )
            for machine_id, item in game["machines"].items()
        }
        ledger = [
            LedgerEntry(
                date=GameDate(**entry["date"]),
                category=entry["category"],
                amount_eur=int(entry["amount_eur"]),
                description=entry["description"],
            )
            for entry in game.get("ledger", [])
        ]
        return FarmState(
            profile_name=game["profile_name"],
            farm_name=game["farm_name"],
            difficulty=game["difficulty"],
            seed=int(game["seed"]),
            date=date,
            cash_eur=int(game["cash_eur"]),
            fields=fields,
            machines=machines,
            inventory_t={key: float(value) for key, value in game.get("inventory_t", {}).items()},
            ledger=ledger,
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise SavegameError(f"invalid savegame structure: {exc}") from exc
