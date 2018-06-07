#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

sense.show_letter("H", (0, g, r) )
time.sleep(1)
sense.show_letter("i", (r, 0, b))
time.sleep(1)
sense.show_letter("!", (b, 0, 0))
time.sleep(1)
sense.clear()

