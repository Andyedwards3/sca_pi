#!/usr/bin/env python

#this script turns the led on and off

import RPi.GPIO as GPIO
import time

#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for auto flash LED: pin11 = GPIO 17

led_pin= 11

# set Auto flash LED pins mode as output
GPIO.setup(led_pin, GPIO.OUT)

#turn on auto flash
GPIO.output(led_pin, True)
time.sleep(4)

#turn off Auto flash LED
GPIO.output(led_pin, False)

#reset GPIO  resources used by script
GPIO. cleanup()
