from base_robot import BaseRobot
from tests import gyro_straight
from pybricks.tools import wait
import settings

def start(bot: BaseRobot):
    settings.kp = 4.90436
    settings.ki = 0.0
    settings.kd = 2.221

    # drive to izzy
    bot.drivebase.straight(90)
    bot.drivebase.turn(-44.5)
    gyro_straight(bot, 240, 80, 25)
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
    bot.left_motor.dc(-80)
    bot.right_motor.dc(-85) # right side gets more power because of resistance
    wait(950)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    # turn and deposit sam
    bot.drivebase.turn(-45.5 - bot.hub.imu.heading())
    gyro_straight(bot, 230, 80, 25)
    bot.hub.imu.reset_heading(0)
    bot.drivebase.curve(500, 30) # avoid crashing into the boat
    bot.drivebase.curve(500, -30)
    bot.drivebase.turn(0 - bot.hub.imu.heading()) # straighten
    gyro_straight(bot, 410, 80, 25)
    bot.drivebase.curve(-255, 88) # curve to the carousel
    bot.left_attach_motor.dc(-80)
    wait(3350)
    bot.left_attach_motor.dc(0)
    # go back to home base and pick up noah
    bot.left_motor.dc(-80)
    bot.right_motor.dc(-80)
    wait(600)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    bot.drivebase.turn(21)
    gyro_straight(bot, 250, 80, 25)
    bot.drivebase.curve(380, 50)
    gyro_straight(bot, 350, 80, 25)
