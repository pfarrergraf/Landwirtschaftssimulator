extends CharacterBody3D

@export var move_speed: float = 5.0
@export var acceleration: float = 18.0
@export var rotation_speed: float = 10.0
@export var camera_sensitivity: float = 0.003
@export var camera_pitch_min: float = deg_to_rad(-55.0)
@export var camera_pitch_max: float = deg_to_rad(25.0)

@onready var camera_pivot: Node3D = $CameraPivot
@onready var player_camera: Camera3D = $CameraPivot/Camera3D
@onready var collision_shape: CollisionShape3D = $CollisionShape3D
@onready var player_mesh: MeshInstance3D = $Mesh
@onready var interaction_prompt: Label = get_node_or_null("../HUD/InteractionPrompt") as Label

var gravity: float = ProjectSettings.get_setting("physics/3d/default_gravity")
var camera_pitch: float = deg_to_rad(-12.0)
var control_enabled: bool = true
var current_vehicle: Node = null
var interaction_candidate: Node = null


func _ready() -> void:
    Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
    camera_pivot.rotation.x = camera_pitch
    _refresh_interaction_prompt()


func _unhandled_input(event: InputEvent) -> void:
    if not control_enabled:
        return
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
    elif event.is_action_pressed("interact"):
        _try_interact()
    elif event.is_action_pressed("save_game"):
        var error := SavegameService.save_player(self)
        print("Savegame result: ", error)
    elif event.is_action_pressed("load_game"):
        print("Savegame loaded: ", SavegameService.load_player(self))


func _physics_process(delta: float) -> void:
    if not control_enabled:
        velocity = Vector3.ZERO
        return

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


func set_interaction_candidate(candidate: Node) -> void:
    if not control_enabled:
        return
    interaction_candidate = candidate
    _refresh_interaction_prompt()


func clear_interaction_candidate(candidate: Node) -> void:
    if interaction_candidate == candidate:
        interaction_candidate = null
        _refresh_interaction_prompt()


func enter_vehicle(vehicle: Node, seat_transform: Transform3D) -> void:
    current_vehicle = vehicle
    interaction_candidate = null
    control_enabled = false
    velocity = Vector3.ZERO
    global_transform = seat_transform
    player_mesh.visible = false
    collision_shape.set_deferred("disabled", true)
    player_camera.current = false
    _refresh_interaction_prompt()


func exit_vehicle(exit_transform: Transform3D) -> void:
    global_transform = exit_transform
    current_vehicle = null
    control_enabled = true
    player_mesh.visible = true
    collision_shape.set_deferred("disabled", false)
    player_camera.current = true
    velocity = Vector3.ZERO
    _refresh_interaction_prompt()


func _try_interact() -> void:
    if interaction_candidate == null or not is_instance_valid(interaction_candidate):
        return
    if interaction_candidate.has_method("request_enter"):
        interaction_candidate.request_enter(self)


func _refresh_interaction_prompt() -> void:
    if interaction_prompt == null:
        return
    var can_interact := (
        control_enabled
        and interaction_candidate != null
        and is_instance_valid(interaction_candidate)
    )
    interaction_prompt.visible = can_interact
    if can_interact and interaction_candidate.has_method("get_interaction_label"):
        interaction_prompt.text = interaction_candidate.get_interaction_label()
