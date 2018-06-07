#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat ()

#rthis script will clear any leds left in the on state that a different script left

sense.clear()
sense.show_message("Hello World!")

