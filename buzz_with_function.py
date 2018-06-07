#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for passive buzzer; pin 32= GPIO12
buzz_pin = 32

#set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin, GPIO.OUT)

#create buzz function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin, 1000)
def buzz(freq):
    Buzz.ChangeFrequency(freq)
    Buzz.start(50)
    time.sleep(1)
    Buzz.stop()

buzz(500)
buzz(300)
buzz(700)


#reset resources used by script
GPIO.cleanup()
