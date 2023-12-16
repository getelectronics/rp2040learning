from machine import Pin
import time

# Initialization of GPIO0 as output
led = Pin(0, Pin.OUT)

# switching on/of the LED
while True:
    led.value(0)
    time.sleep(2)
    led.value(1)
    time.sleep(10)