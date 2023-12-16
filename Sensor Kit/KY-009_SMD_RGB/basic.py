from machine import Pin, PWM
from time import sleep

# Initialization of GPIO0, GPIO1 and GPIO2 as outputs
Red = Pin(0, Pin.OUT)
Green = Pin(1, Pin.OUT)
Blue = Pin(2, Pin.OUT)

# individual LED colors
def singleLeds():
    Red.value(1)
    Green.value(0)
    Blue.value(0)
    sleep(3)
    Red.value(0)
    Green.value(1)
    Blue.value(0)
    sleep(3)
    Red.value(0)
    Green.value(0)
    Blue.value(1)
    sleep(3)
    Red.value(0)
    Green.value(0)
    Blue.value(0)

# mix the leds to make new colors.
def multiLeds():
    Green.value(1)
    Red.value(1)
    Blue.value(0)
    sleep(3)
    Green.value(1)
    Red.value(0)
    Blue.value(1)
    sleep(3)
    Green.value(0)
    Red.value(1)
    Blue.value(1)
    sleep(3)
    Green.value(0)
    Red.value(0)
    Blue.value(0)
    
while True:
    singleLeds()
    sleep(3)
    multiLeds()