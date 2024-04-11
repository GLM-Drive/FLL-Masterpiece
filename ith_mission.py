from pybricks.tools import wait
from tests import gyro_straight, turn
from base_robot import BaseRobot
import settings

def start(bot: BaseRobot):
    turn(bot, 50)
    gyro_straight(bot, 650, 80, 25)
    turn(bot, 40)
    gyro_straight(bot, 100, 80, 25)
    bot.left_motor.dc(75)
    bot.right_motor.dc(75)
    bot.left_attach_motor.dc(100)
    wait(3000)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    bot.left_attach_motor.dc(0)
    bot.drivebase.straight(-150)
    turn(bot, -45)
    bot.drivebase.straight(-900)
    bot.drivebase.brake()
