from machine import Pin, Timer
import time

# Initialization of GPIO28 as input
button = Pin(28, Pin.IN, Pin.PULL_DOWN)

# Timer initialization
timer = Timer()
# Variables initialization
i = 0

def func(pin):
    global i
    i = i + 1
    print(i)


if button.value() == 1:
    # Initialization interrupt
    button.irq(handler=func, trigger=button.IRQ_FALLING)

# REPL
print("Tap the sensor")
print("-------------------------------------")