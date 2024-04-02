from base_robot import BaseRobot
from pybricks.tools import wait
from tests import gyro_straight

def start(bot: BaseRobot):
    gyro_straight(bot, 350, 70, 25)
    bot.left_attach_motor.dc(-100)
    wait(800)
    bot.left_attach_motor.dc(0)
    bot.drivebase.straight(-90)
    bot.hub.imu.reset_heading(0)
    bot.drivebase.turn(-40 - bot.hub.imu.heading())
    bot.left_attach_motor.dc(100)
    wait(300)
    bot.left_attach_motor.dc(0)
    bot.drivebase.curve(-150, -30)
    bot.drivebase.straight(-300)
    bot.drivebase.brake()
