from base_robot import BaseRobot
from pybricks.parameters import Button

print("Initializing...")
base_robot = BaseRobot()

print("Battery:")
print(f"{base_robot.hub.battery.voltage()}mV")
print(f"{base_robot.hub.battery.current()}mA")

base_robot.hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

while(True):
    base_robot.prompt()
