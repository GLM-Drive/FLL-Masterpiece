from base_robot import BaseRobot
from tests import gyro_straight, turn
from pybricks.tools import wait
import settings

def start(bot: BaseRobot):
    # drive to izzy
    turn(bot, -44, 37.5)
    gyro_straight(bot, 300, 80, 25)
    # pick up izzy
    bot.right_attach_motor.dc(-80)
    wait(350)
    bot.right_attach_motor.dc(0)
    bot.drivebase.straight(90)
    wait(100)
    # turn chicken
    bot.left_attach_motor.dc(-100)
    bot.left_motor.dc(65)
    bot.right_motor.dc(65)
    wait(5800)
    bot.left_attach_motor.dc(0)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    wait(100)
    # go back
    bot.hub.imu.reset_heading(0)
    bot.left_motor.dc(-80)
    bot.right_motor.dc(-80)
    wait(1500)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    wait(3000) # time to realign
    # goto sam
    turn(bot, -75, base_speed=35)
    gyro_straight(bot, 825, 80, 25)
    turn(bot, 8, base_speed=35)
    # go to other home base and take sam with it
    bot.drivebase.curve(420, -53)
    gyro_straight(bot, 400, 80, 25)
    bot.drivebase.brake()
