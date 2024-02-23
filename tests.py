from base_robot import BaseRobot
from pybricks.tools import wait, StopWatch
import settings

def gyro_straight(bot: BaseRobot, distance: int, speed: int, accel: int, kp: float = settings.kp, ki: float = settings.ki, kd: float = settings.kd):
    integral = 0
    prev_error = 0
    total_error = 0 

    timer = StopWatch()
    decel_start = 0

    bot.hub.imu.reset_heading(0)
    while (bot.drivebase.distance() < distance):
        error = bot.hub.imu.heading()
 
        if (error == 0):
            integral = 0
        else:
            integral = integral + error 
 
        derivative = error - prev_error  
 
        correction = ((kp * error) + (ki * integral) + (kd * derivative)) * -1
 
        power = speed
        if bot.drivebase.distance() / distance <= 0.30:
            power = min(accel * (timer.time() / 1000), speed)

        elif bot.drivebase.distance() / distance >= 0.70:
            if decel_start == 0:
                decel_start = timer.time()
            power = max(1, speed - accel * ((timer.time() - decel_start) / 1000))

        power_left = power + correction
        power_right = power - correction

        bot.left_motor.dc(power_left) 
        bot.right_motor.dc(power_right)

        total_error += abs(error)

        prev_error = error  
        wait(10)

    bot.drivebase.stop()
    bot.drivebase.reset()
    return total_error

def pid_tune(base_robot: BaseRobot, distance: int, speed: int, accel: int, tol=0.2):
    p = [0.0, 0.0, 0.0]
    dp = [1.0, 1.0, 1.0]
    best_error = gyro_straight(base_robot, distance, speed, accel, p[0], p[1], p[2])

    while sum(dp) > tol:
        for i in range(len(p)):
            p[i] += dp[i]
            error = gyro_straight(base_robot, distance, speed, accel, p[0], p[1], p[2])

            if error < best_error:
                best_error = error
                dp[i] *= 1.1
            else:
                p[i] -= 2 * dp[i]
                error = gyro_straight(base_robot, distance, speed, accel, p[0], p[1], p[2])

                if error < best_error:
                    best_error = error
                    dp[i] *= 1.1
                else:
                    p[i] += dp[i]
                    dp[i] *= 0.9
    return p
