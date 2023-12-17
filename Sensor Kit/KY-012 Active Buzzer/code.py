from machine import Pin
from utime import sleep

# Initialization of GPIO28 as output
buzzer = Pin(28, Pin.OUT, value=0)

# Switch on buzzer
print("ON")
buzzer.on()

# Wait 3 seconds
print("Wait for 3 seconds")
sleep(3)

# Switch off buzzer
print("OFF")
buzzer.off()