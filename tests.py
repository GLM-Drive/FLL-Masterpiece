from base_robot import BaseRobot
from pybricks.tools import wait

def gyro_straight(bot: BaseRobot, distance: int, speed: int):
    
    kp = 3     
    ki = 0.025
    kd = 3

    integral = 0
    prev_error = 0

    bot.hub.imu.reset_heading(0)
    while (bot.drivebase.distance() < distance):
        error = bot.hub.imu.heading() 

        if (error == 0):
            integral = 0
        else:
            integral = integral + error 
        
        derivative = error - prev_error  

        correction = ((kp * error) + (ki * integral) + (kd * derivative)) * -1

        power_left = speed + correction
        power_right = speed - correction   

        bot.left_motor.dc(power_left) 
        bot.right_motor.dc(power_right) 
     
        prev_error = error  
        wait(10)
   
    bot.drivebase.stop()
