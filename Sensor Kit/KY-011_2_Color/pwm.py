import machine
import math

# Initialization of GPIO0 and GPIO1 as PWM pins
Red = machine.PWM(machine.Pin(0))
Red.freq(1000)
Green = machine.PWM(machine.Pin(1))
Green.freq(1000)

RG = [0,0]

def sinColour(number):
    a = (math.sin(math.radians(number))+1)*32768
    c = (math.sin(math.radians(number+90))+1)*32768
    RG = (int(a),int(c))
    return RG

# Infinite loop
a = 0
while True:
    RG = sinColour(a)
    a = a + 0.01
    if a == 360:
        a = 0
    Red.duty_u16(RG[0])
    Green.duty_u16(RG[1])