from pybricks.parameters import Port, Direction

# Robot Hardware
wheel_diameter = 61
axle_track = 83

# Driving
precision_profile = 6
straight_speed = 400 # mm/s
straight_accel = 600 # mm/s²
turn_rate = 150 # deg/s
# turn_accel = 360 # deg/s² # breaks the drivebase for some reason

kp = 5.466601
ki = 0.5314411
kd = -3.372691

# Motor Settings
left_motor_port = Port.E
left_motor_direction = Direction.COUNTERCLOCKWISE
left_motor_gears = []

right_motor_port = Port.D
right_motor_direction = Direction.CLOCKWISE
right_motor_gears = []

left_attach_motor_port = Port.B
left_attach_motor_direction = Direction.COUNTERCLOCKWISE

right_attach_motor_port = Port.F
right_attach_motor_direction = Direction.CLOCKWISE
