import tests
from base_robot import BaseRobot
from pybricks.parameters import Button
from pybricks.tools import hub_menu, wait

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
            print("Running mission one.")
        elif selected == "2":
            while not base_robot.hub.imu.ready():
                print("not ready")
                wait(100)
            tests.gyro_straight(base_robot, 1500, 80, 50)
        elif selected == "3":
            print(tests.pid_tune(base_robot, 500, 80, 50))
        elif selected == "X":
            break
        elif selected == "G":
            while True:
                print(base_robot.hub.imu.heading())
