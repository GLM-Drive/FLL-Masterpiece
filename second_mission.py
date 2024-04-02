from base_robot import BaseRobot
from tests import gyro_straight
from pybricks.tools import wait

def start(bot: BaseRobot):
    bot.drivebase.turn(47)
    gyro_straight(bot, 460, 100, 100)
    bot.left_motor.dc(100)
    bot.right_motor.dc(80)
    wait(500)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    bot.left_motor.dc(-100)
    bot.right_motor.dc(-100)
    wait(1500)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
