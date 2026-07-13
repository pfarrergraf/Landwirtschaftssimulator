from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_godot_spike_has_camera_and_savegame_contract() -> None:
    project = (ROOT / "game/godot/project.godot").read_text(encoding="utf-8")
    controller = (ROOT / "game/godot/scripts/player_controller.gd").read_text(encoding="utf-8")
    savegame = (ROOT / "game/godot/scripts/savegame_service.gd").read_text(encoding="utf-8")

    assert 'run/main_scene="res://scenes/main.tscn"' in project
    assert "toggle_mouse_capture" in project
    assert "save_game" in project
    assert "load_game" in project
    assert "InputEventMouseMotion" in controller
    assert "SavegameService.save_player" in controller
    assert "SavegameService.load_player" in controller
    assert "SCHEMA_VERSION: int = 1" in savegame
    assert 'SAVE_PATH: String = "user://mvp_savegame.json"' in savegame
    assert 'temporary_path := SAVE_PATH + ".tmp"' in savegame
