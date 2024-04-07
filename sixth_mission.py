from pybricks.tools import wait, StopWatch
from tests import gyro_straight
from base_robot import BaseRobot

def start(bot: BaseRobot):
    turn(bot, 46, 35)
    bot.hub.imu.reset_heading(0)
    gyro_straight(bot, 1150, 80, 25)
    turn(bot, -46 + bot.hub.imu.heading())
    bot.drivebase.straight(30)
    bot.drivebase.straight(-70)

    bot.drivebase.curve(-110, -90)
    bot.drivebase.straight(-120)
    bot.drivebase.curve(-110, 90)
    gyro_straight(bot, 500, 100, 25)
    
    bot.left_motor.dc(100)
    wait(750)
    bot.right_motor.dc(100)
    bot.left_motor.dc(0)
    wait(750)
    bot.right_motor.dc(0)

    bot.drivebase.straight(-110)
    turn(bot, 88.5)
    bot.drivebase.straight(650, wait=False)
    bot.left_attach_motor.dc(100)
    wait(700)
    bot.left_attach_motor.dc(0)
    wait(1800)

    bot.drivebase.curve(220, 45)
    bot.drivebase.straight(-550)
    bot.drivebase.curve(1500, 40)
    bot.drivebase.brake()

def turn(bot: BaseRobot, angle: float, base_speed: float = 25):
    bot.hub.imu.reset_heading(0)
    timer = StopWatch()
    curr_angle = bot.hub.imu.heading()
    tol = 0.50
    while(abs(curr_angle - angle) > tol):
        curr_angle = bot.hub.imu.heading()
        if timer.time() >= 1000:
            tol = 2
        if timer.time() >= 1500:
            tol = 4
        if timer.time() >= 2500:
            break
        print(f"curr: {curr_angle} want: {angle} tol: {tol}")
        bot.left_motor.dc(base_speed + angle - curr_angle)
        bot.right_motor.dc(base_speed + -(angle - curr_angle))
    bot.left_motor.dc(0)
    bot.right_motor.dc(0)
