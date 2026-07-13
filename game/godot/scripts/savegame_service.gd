class_name SavegameService
extends RefCounted

const SCHEMA_VERSION: int = 1
const SAVE_PATH: String = "user://mvp_savegame.json"


static func save_player(player: Node3D) -> Error:
    var payload := {
        "schema_version": SCHEMA_VERSION,
        "player": {
            "position": [player.global_position.x, player.global_position.y, player.global_position.z],
            "rotation_y": player.global_rotation.y,
        },
    }
    var temporary_path := SAVE_PATH + ".tmp"
    var file := FileAccess.open(temporary_path, FileAccess.WRITE)
    if file == null:
        return FileAccess.get_open_error()
    file.store_string(JSON.stringify(payload))
    file.flush()
    file.close()
    if FileAccess.file_exists(SAVE_PATH):
        DirAccess.remove_absolute(SAVE_PATH)
    return DirAccess.rename_absolute(temporary_path, SAVE_PATH)


static func load_player(player: Node3D) -> bool:
    if not FileAccess.file_exists(SAVE_PATH):
        return false
    var file := FileAccess.open(SAVE_PATH, FileAccess.READ)
    if file == null:
        return false
    var parsed: Variant = JSON.parse_string(file.get_as_text())
    if not parsed is Dictionary:
        return false
    var data: Dictionary = parsed
    if int(data.get("schema_version", 0)) != SCHEMA_VERSION:
        return false
    var player_data: Dictionary = data.get("player", {})
    var position_data: Array = player_data.get("position", [])
    if position_data.size() != 3:
        return false
    player.global_position = Vector3(
        float(position_data[0]),
        float(position_data[1]),
        float(position_data[2])
    )
    player.global_rotation.y = float(player_data.get("rotation_y", 0.0))
    return true
