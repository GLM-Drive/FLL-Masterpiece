from base_robot import BaseRobot
from tests import gyro_straight, turn
from pybricks.tools import wait
import settings

def start(bot: BaseRobot):
    prev_p = settings.kp
    prev_i = settings.ki
    prev_d = settings.kd
    #settings.kp = 4.90436
    #settings.ki = 0.0
    #settings.kd = 2.221
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
    bot.left_motor.dc(75)
    bot.right_motor.dc(75)
    wait(5800)
    bot.left_attach_motor.dc(0)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    wait(100)
    # go back
    bot.hub.imu.reset_heading(0)
    bot.drivebase.straight(-350)
    turn(bot, -45 - bot.hub.imu.heading(), 35)
    # pick up sam
    gyro_straight(bot, 100, 80, 25)
    turn(bot, 18, 35)
    # go to noah
    gyro_straight(bot, 825, 80, 25)
    turn(bot, -35)
    # return home
    gyro_straight(bot, 500, 80, 25)
    bot.drivebase.brake()
    settings.kp = prev_p
    settings.ki = prev_i
    settings.kd = prev_d
