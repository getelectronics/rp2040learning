from machine import Pin, PWM
from time import sleep

# Initialization of GPIO0 and GPIO1 as output
Green = Pin(1, Pin.OUT)
Red = Pin(0, Pin.OUT)

while True:
    Green.value(1)
    Red.value(0)
    sleep(1)
    Green.value(0)
    Red.value(1)
    sleep(1)
    Green.value(0)
    Red.value(0)