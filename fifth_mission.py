from tests import gyro_straight
from pybricks.tools import wait
from base_robot import BaseRobot

def start(bot: BaseRobot):
    bot.drivebase.straight(800)
    bot.left_motor.dc(100)
    wait(500)
    bot.left_motor.dc(0)
    bot.drivebase.straight(-400)
    bot.drivebase.brake()
