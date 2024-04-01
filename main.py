import tests
from base_robot import BaseRobot
from pybricks.parameters import Button
from pybricks.tools import hub_menu, wait
import first_mission

print("Initializing...")
base_robot = BaseRobot()

print("Battery:")
print(f"{base_robot.hub.battery.voltage()}mV")
print(f"{base_robot.hub.battery.current()}mA")

base_robot.hub.system.set_stop_button(Button.BLUETOOTH)
first_mission.start(base_robot)

while(False):
        print("Waiting for user to select a mission.")
        selected = hub_menu("1", "2", "3", "X", "G")
        print("back in loop")
        if selected == "1":
            print("1 selected")
            first_mission.start(base_robot)
            print("1 done")
        elif selected == "2":
            while not base_robot.hub.imu.ready():
                print("not ready")
                wait(100)
            tests.gyro_straight(base_robot, 2000, 80, 50)
        elif selected == "3":
            print(tests.pid_tune(base_robot, 1000, 80, 25))
        elif selected == "X":
            break
        elif selected == "G":
            while True:
                print(base_robot.hub.imu.heading())
