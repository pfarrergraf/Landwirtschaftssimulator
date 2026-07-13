from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_vehicle_interaction_spike_has_clean_input_ownership() -> None:
    project = (ROOT / "game/godot/project.godot").read_text(encoding="utf-8")
    scene = (ROOT / "game/godot/scenes/main.tscn").read_text(encoding="utf-8")
    player = (ROOT / "game/godot/scripts/player_controller.gd").read_text(encoding="utf-8")
    tractor = (ROOT / "game/godot/scripts/generic_tractor.gd").read_text(encoding="utf-8")

    assert "interact={" in project
    assert 'physical_keycode":69' in project
    for node_name in (
        'name="GenericTractor"',
        'name="SeatMarker"',
        'name="ExitMarker"',
        'name="VehicleCamera"',
        'name="InteractionArea"',
        'name="InteractionPrompt"',
    ):
        assert node_name in scene

    assert "control_enabled: bool = true" in player
    assert "func set_interaction_candidate" in player
    assert "func enter_vehicle" in player
    assert "func exit_vehicle" in player
    assert "player_camera.current = false" in player

    assert "driver: Node3D = null" in tractor
    assert "func request_enter" in tractor
    assert "func exit_driver" in tractor
    assert "vehicle_camera.current = true" in tractor
    assert "driver.global_transform = seat_marker.global_transform" in tractor


def test_tractor_blockout_is_brand_neutral() -> None:
    paths = (
        ROOT / "game/godot/scenes/main.tscn",
        ROOT / "game/godot/scripts/generic_tractor.gd",
    )
    combined = "\n".join(path.read_text(encoding="utf-8") for path in paths)
    for restricted_brand in (
        "Fendt",
        "John Deere",
        "CLAAS",
        "Deutz",
        "Case IH",
        "New Holland",
    ):
        assert restricted_brand not in combined
