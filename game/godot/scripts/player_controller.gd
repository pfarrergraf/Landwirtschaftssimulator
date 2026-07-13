extends CharacterBody3D

@export var move_speed: float = 5.0
@export var acceleration: float = 18.0
@export var rotation_speed: float = 10.0
@export var camera_sensitivity: float = 0.003
@export var camera_pitch_min: float = deg_to_rad(-55.0)
@export var camera_pitch_max: float = deg_to_rad(25.0)

@onready var camera_pivot: Node3D = $CameraPivot

var gravity: float = ProjectSettings.get_setting("physics/3d/default_gravity")
var camera_pitch: float = deg_to_rad(-12.0)


func _ready() -> void:
    Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
    camera_pivot.rotation.x = camera_pitch


func _unhandled_input(event: InputEvent) -> void:
    if event is InputEventMouseMotion and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
        rotate_y(-event.relative.x * camera_sensitivity)
        camera_pitch = clamp(
            camera_pitch - event.relative.y * camera_sensitivity,
            camera_pitch_min,
            camera_pitch_max
        )
        camera_pivot.rotation.x = camera_pitch
    elif event.is_action_pressed("toggle_mouse_capture"):
        Input.mouse_mode = (
            Input.MOUSE_MODE_VISIBLE
            if Input.mouse_mode == Input.MOUSE_MODE_CAPTURED
            else Input.MOUSE_MODE_CAPTURED
        )
    elif event.is_action_pressed("save_game"):
        var error := SavegameService.save_player(self)
        print("Savegame result: ", error)
    elif event.is_action_pressed("load_game"):
        print("Savegame loaded: ", SavegameService.load_player(self))


func _physics_process(delta: float) -> void:
    var input_vector := Input.get_vector(
        "move_left",
        "move_right",
        "move_forward",
        "move_backward"
    )
    var local_direction := Vector3(input_vector.x, 0.0, input_vector.y)
    var direction := global_transform.basis * local_direction
    direction.y = 0.0

    if direction.length_squared() > 0.0:
        direction = direction.normalized()
        velocity.x = move_toward(velocity.x, direction.x * move_speed, acceleration * delta)
        velocity.z = move_toward(velocity.z, direction.z * move_speed, acceleration * delta)
    else:
        velocity.x = move_toward(velocity.x, 0.0, acceleration * delta)
        velocity.z = move_toward(velocity.z, 0.0, acceleration * delta)

    if not is_on_floor():
        velocity.y -= gravity * delta
    else:
        velocity.y = 0.0

    move_and_slide()
