from pybricks.tools import wait
from base_robot import BaseRobot
from tests import gyro_straight
import settings

def start(bot: BaseRobot):
    # leave base
    bot.drivebase.straight(100)
    bot.drivebase.turn(30)
    gyro_straight(bot, 740, 80, 25)
    # make sure izzy is on the skateboard
    bot.drivebase.turn(30)
    bot.drivebase.straight(90)
    bot.drivebase.straight(-90)
    bot.drivebase.turn(-30)
    # go to scene change thing
    bot.drivebase.straight(-120)
    bot.drivebase.turn(-77)
    bot.drivebase.straight(160)
    # pick up emily
    bot.right_attach_motor.dc(-100)
    wait(500)
    bot.right_attach_motor.dc(0)
    # make sure scene change thing got pressed
    bot.left_motor.dc(100)
    bot.right_motor.dc(100)
    wait(400)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    # go back to home base
    bot.left_motor.dc(-50)
    bot.right_motor.dc(-50)
    wait(300)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    bot.drivebase.settings(turn_rate=150)
    bot.drivebase.turn(65)
    bot.drivebase.settings(turn_rate=settings.turn_rate)
    bot.drivebase.straight(-750)
    bot.drivebase.brake()
