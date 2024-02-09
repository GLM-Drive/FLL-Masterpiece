import settings

from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.hubs import PrimeHub

class BaseRobot():
    def __init__(self):
        self.hub = PrimeHub()
        self.left_motor = Motor(port=settings.left_motor_port, positive_direction=settings.left_motor_direction, gears=settings.left_motor_gears, reset_angle=True, profile=settings.precision_profile)
        self.right_motor = Motor(port=settings.right_motor_port, positive_direction=settings.right_motor_direction, gears=settings.right_motor_gears, reset_angle=True, profile=settings.precision_profile)
        self.drivebase = DriveBase(left_motor=self.left_motor, right_motor=self.right_motor, wheel_diameter=settings.wheel_diameter, axle_track=settings.axle_track)
        self.drivebase.use_gyro(True)
        self.drivebase.settings(straight_speed=settings.straight_speed, straight_acceleration=settings.straight_accel, turn_rate=settings.turn_rate)#, turn_acceleration=settings.turn_accel)
        self.left_attach_motor = Motor(port=settings.left_attach_motor_port, positive_direction=settings.left_attach_motor_direction, reset_angle=True, profile=settings.precision_profile)
        self.right_attach_motor = Motor(port=settings.right_attach_motor_port, positive_direction=settings.right_attach_motor_direction, reset_angle=True, profile=settings.precision_profile)
