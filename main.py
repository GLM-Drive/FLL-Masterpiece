import tests
from base_robot import BaseRobot
from pybricks.parameters import Button
from pybricks.tools import hub_menu, wait
import first_mission
import second_mission
import third_mission
import settings

print("Initializing...")
base_robot = BaseRobot()

print("Battery:")
print(f"{base_robot.hub.battery.voltage()}mV")
print(f"{base_robot.hub.battery.current()}mA")

base_robot.hub.system.set_stop_button(Button.BLUETOOTH)

while(True):
        print("Waiting for user to select a mission.")
        selected = hub_menu("1", "2", "3", "X", "G")
        if selected == "1":
            first_mission.start(base_robot)
        elif selected == "2":
            second_mission.start(base_robot)
        elif selected == "3":
            third_mission.start(base_robot)
        elif selected == "X":
            break
        elif selected == "G":
            settings.kp = 4.90436
            settings.ki = 0.0
            settings.kd = 2.221
            tests.gyro_straight(base_robot, 1000, 80, 25)
