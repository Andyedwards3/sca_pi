#!/usr/bin/env python
from sense_hat import SenseHat
import random
sense = SenseHat()
message = 'HI'
speed = 0.01
yellow = (255, 255, 0)
blue = (0, 0, 255 )
sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
user_guess = raw_input('What is your guess?')

while message != user_guess:

    yellow = (255, 255, 0)
    blue = (0, 0, 255 )

    
    
    sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
    user_guess = raw_input('What is your guess?')

    speed = 0.01
    yellow = (255, 255, 0)
    blue = (0, 0, 255 )

    speed = 0.03
    
    sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
    user_guess = raw_input('What is your guess?')
sense.clear()






