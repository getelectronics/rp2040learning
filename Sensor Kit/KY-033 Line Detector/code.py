from machine import Pin
from time import sleep

# Initialization of GPIO27 as input
sensor = Pin(27, Pin.IN, Pin.PULL_DOWN)

# Continuous loop
while True:
    if sensor.value() == 0:
        print("No line present")
    else:
        print("Line present")

    print("-------------------------------------")
    sleep(1)