from machine import Pin, Timer

# Initialization of GPIO 28 as input
sensor = Pin(28, Pin.IN, Pin.PULL_DOWN)

# Create timer
timer = Timer()

# Set counter to 0
counter = 0


def tilt(timer):
    global counter
    counter = counter + 1
    print("Tilt detected")
    print(counter)

# Function: debounce
def debounce(pin):
    # Debounce function: Set timer
    timer.init(mode=Timer.ONE_SHOT, period=100, callback=tilt)

# Interrupt
while True:
    sensor.irq(trigger=Pin.IRQ_FALLING, handler=debounce)