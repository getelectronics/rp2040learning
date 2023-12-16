import machine
import math

# Initialization of GPIO0, GPIO1 and GPIO2 as PWM Pin
Red = machine.PWM(machine.Pin(0))
Red.freq(1000)
Green = machine.PWM(machine.Pin(1))
Green.freq(1000)
Blue = machine.PWM(machine.Pin(2))
Blue.freq(1000)

RGB = [0,0,0]

def sinColour(number):
    a = (math.sin(math.radians(number))+1)*32768
    b = (math.sin(math.radians(number+120))+1)*32768
    c = (math.sin(math.radians(number+240))+1)*32768
    RGB = (int(a),int(b),int(c))
    return RGB

# Endless loop
a = 0
while True:
    RGB = sinColour(a)
    a += 0.01
    if a == 360:
        a = 0
    Red.duty_u16(RGB[0])
    Green.duty_u16(RGB[1])
    Blue.duty_u16(RGB[2])