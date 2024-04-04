import tests
from base_robot import BaseRobot
from pybricks.parameters import Button
from pybricks.tools import hub_menu, wait
import first_mission
import ith_mission
import second_mission
import third_mission
import fourth_mission
import fifth_mission
import sixth_mission
import seventh_mission
import eighth_mission
import settings

print("Initializing...")
base_robot = BaseRobot()

print("Battery:")
print(f"{base_robot.hub.battery.voltage()}mV")
print(f"{base_robot.hub.battery.current()}mA")

base_robot.hub.system.set_stop_button(Button.BLUETOOTH)

prev_selected = "1"
while(True):
        print("Waiting for user to select a mission.")
        missions = [ "1", "I", "2", "3", "4", "5", "6", "7", "8", "X", "C", "G" ]
        index = missions.index(prev_selected)
        missions = missions[index:] + missions[:index]
        selected = hub_menu(*missions)
        prev_selected = selected
        if selected == "1":
            first_mission.start(base_robot)
        elif selected == "I":
            ith_mission.start(base_robot)
        elif selected == "2":
            second_mission.start(base_robot)
        elif selected == "3":
            third_mission.start(base_robot)
        elif selected == "4":
            fourth_mission.start(base_robot)
        elif selected == "5":
            fifth_mission.start(base_robot)
        elif selected == "6":
            sixth_mission.start(base_robot)
        elif selected == "7":
            seventh_mission.start(base_robot)
        elif selected == "8":
            settings.kp = 5.93666
            settings.ki = 0.0
            settings.kd = 0.01870095
            eighth_mission.start(base_robot)
        elif selected == "X":
            break
        elif selected == "G":
            tests.gyro_straight(base_robot, 1000, 80, 25)
        elif selected == "C":
            print(tests.pid_tune(base_robot, 1000, 80, 25))
