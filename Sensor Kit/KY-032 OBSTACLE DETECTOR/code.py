from machine import Pin, Timer
from time import sleep

# Initialization of GPIO27 as input
sensor = Pin(27, Pin.IN, Pin.PULL_DOWN)

# Continuous loop
while True:
    if sensor.value() == 0:
        print("Obstacle detected")
    else:
        print("No obstacle detected")

    print("-------------------")
    sleep(0.5)