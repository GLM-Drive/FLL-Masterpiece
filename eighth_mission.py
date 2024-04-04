from pybricks.tools import wait
from base_robot import BaseRobot
from tests import gyro_straight, turn
import settings

def start(bot: BaseRobot):
    prev_p = settings.kp
    prev_i = settings.ki
    prev_d = settings.kd
    settings.kp = 5.93666
    settings.ki = 0.0
    settings.kd = 0.01870095
    gyro_straight(bot, 600, 80, 25)
    bot.left_motor.dc(75)
    bot.right_motor.dc(75)
    wait(1000)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)

    bot.right_attach_motor.dc(100)
    bot.left_motor.dc(85)
    bot.right_motor.dc(85)
    wait(250)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    wait(1000)
    bot.right_attach_motor.dc(0)
    bot.drivebase.straight(-175)
    turn(bot, -45)
    bot.drivebase.curve(1150, 20)
    bot.drivebase.brake()
    settings.kp = prev_p
    settings.ki = prev_i
    settings.kd = prev_d
