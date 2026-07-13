class_name GenericTractor
extends CharacterBody3D

@export var maximum_speed: float = 10.0
@export var acceleration: float = 6.0
@export var braking: float = 9.0
@export var steering_speed: float = 1.25
@export var camera_sensitivity: float = 0.003
@export var camera_pitch_min: float = deg_to_rad(-45.0)
@export var camera_pitch_max: float = deg_to_rad(20.0)

@onready var seat_marker: Marker3D = $SeatMarker
@onready var exit_marker: Marker3D = $ExitMarker
@onready var vehicle_camera: Camera3D = $CameraPivot/VehicleCamera
@onready var camera_pivot: Node3D = $CameraPivot
@onready var interaction_area: Area3D = $InteractionArea

var gravity: float = ProjectSettings.get_setting("physics/3d/default_gravity")
var driver: Node3D = null
var camera_pitch: float = deg_to_rad(-10.0)


func _ready() -> void:
    interaction_area.body_entered.connect(_on_interaction_body_entered)
    interaction_area.body_exited.connect(_on_interaction_body_exited)
    vehicle_camera.current = false
    camera_pivot.rotation.x = camera_pitch


func _unhandled_input(event: InputEvent) -> void:
    if driver == null:
        return
    if event is InputEventMouseMotion and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
        camera_pivot.rotate_y(-event.relative.x * camera_sensitivity)
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
        exit_driver()


func _physics_process(delta: float) -> void:
    if driver == null:
        velocity.x = move_toward(velocity.x, 0.0, braking * delta)
        velocity.z = move_toward(velocity.z, 0.0, braking * delta)
    else:
        _apply_driver_input(delta)

    if not is_on_floor():
        velocity.y -= gravity * delta
    else:
        velocity.y = 0.0

    move_and_slide()
    if driver != null:
        driver.global_transform = seat_marker.global_transform


func request_enter(player: Node3D) -> void:
    if driver != null or not player.has_method("enter_vehicle"):
        return
    driver = player
    player.enter_vehicle(self, seat_marker.global_transform)
    vehicle_camera.current = true


func exit_driver() -> void:
    if driver == null:
        return
    var exiting_player := driver
    driver = null
    vehicle_camera.current = false
    exiting_player.exit_vehicle(exit_marker.global_transform)
    if exiting_player.has_method("set_interaction_candidate"):
        exiting_player.set_interaction_candidate(self)


func get_interaction_label() -> String:
    return "E: In den Traktor einsteigen"


func _apply_driver_input(delta: float) -> void:
    var throttle := Input.get_axis("move_backward", "move_forward")
    var steering := Input.get_axis("move_right", "move_left")
    var forward := -global_transform.basis.z
    var target_velocity := forward * throttle * maximum_speed
    var rate := acceleration if absf(throttle) > 0.01 else braking

    velocity.x = move_toward(velocity.x, target_velocity.x, rate * delta)
    velocity.z = move_toward(velocity.z, target_velocity.z, rate * delta)

    if absf(throttle) > 0.01:
        rotate_y(steering * steering_speed * delta * signf(throttle))


func _on_interaction_body_entered(body: Node3D) -> void:
    if driver == null and body.has_method("set_interaction_candidate"):
        body.set_interaction_candidate(self)


func _on_interaction_body_exited(body: Node3D) -> void:
    if body.has_method("clear_interaction_candidate"):
        body.clear_interaction_candidate(self)
