#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

x = random.randint(0,7)
y = random.randint(0,7)

sense.set_pixel(2, 2, (0, 0, 255))
time.sleep(0.5)
sense.clear()
sense.set_pixel(2, 4, (0, 255,  0))
time.sleep(0.5)

sense.clear()

sense.set_pixel(3, 4, (255, 255, 0))
time.sleep(.10)
sense.clear()

