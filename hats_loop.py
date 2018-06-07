#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)


x = 1
while x < 2:
    sense.show_letter("H", (r, 0, 0))
print "Random number", r
time.sleep(1)
x = x + 1

sense.clear()
