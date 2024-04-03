from pybricks.tools import wait
from base_robot import BaseRobot
from tests import gyro_straight

def start(bot: BaseRobot):
    bot.drivebase.straight(900)
    bot.drivebase.straight(-900)
    bot.drivebase.brake()
