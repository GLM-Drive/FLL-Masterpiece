from base_robot import BaseRobot
from tests import gyro_straight
from pybricks.tools import wait
import settings

def start(bot: BaseRobot):
    settings.kp = 4.90436
    settings.ki = 0.0
    settings.kd = 2.221

 #   p 2.11089 ki 0.0 kd 2.221
  #  kp 4.90436 ki 0.0 kd 2.221 error 96.1543 tol 0.7244668

    # drive to izzy
    bot.drivebase.straight(90)
    bot.drivebase.turn(-44.5)
    gyro_straight(bot, 240, 80, 25)
    # pick up izzy
    bot.right_attach_motor.dc(-100)
    wait(350)
    bot.right_attach_motor.dc(0)
    bot.drivebase.straight(90)
    wait(100)
    # turn chicken
    bot.left_attach_motor.dc(100)
    bot.left_motor.dc(75)
    bot.right_motor.dc(75)
    wait(3800)
    bot.left_attach_motor.dc(0)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    wait(100)
    # go back
    bot.hub.imu.reset_heading(0)
    bot.left_motor.dc(-80)
    bot.right_motor.dc(-85) # right side gets more power because of resistance
    wait(1250)
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
    # turn
    bot.drivebase.turn(-45 - bot.hub.imu.heading())
    gyro_straight(bot, 300, 80, 25)
    bot.drivebase.curve(850, 12)