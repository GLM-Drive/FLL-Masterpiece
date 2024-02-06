from pybricks.parameters import Port, Direction

# Robot Hardware
wheel_diameter = 40.0
axle_track = 5.0

# Driving
precision_profile = 6
straight_speed = 400 # mm/s
straight_accel = 600 # mm/s²
turn_rate = 150 # deg/s
turn_accel = 360 # deg/s²

# Motor Settings
left_motor_port = Port.D
left_motor_direction = Direction.COUNTERCLOCKWISE
left_motor_gears = []

right_motor_port = Port.E
right_motor_direction = Direction.CLOCKWISE
right_motor_gears = []

left_attach_motor_port = Port.A
left_attach_motor_direction = Direction.COUNTERCLOCKWISE

right_attach_motor_port = Port.B
right_attach_motor_direction = Direction.CLOCKWISE
