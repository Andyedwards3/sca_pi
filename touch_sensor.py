#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#setup
GPIO.setmode(GPIO.BOARD)
GPIO. setwarnings(False)

#assign pin number
touch_pin = 31

#set as input
GPIO.setup(touch_pin, GPIO. IN)

#create loop that reads touch switch
while True:
        if GPIO.input(touch_pin) == 0 :
            buzz_pin = 32

#set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin, GPIO.OUT)

#create buzz function and set initial sound frequency to 1000 Hz
Buzz = GPIO. PWM(buzz_pin, 1000)
Buzz.ChangeFrequency(550)

#change frequency and start passive buzzer using buzz function with 50% duty for 1 second
Buzz.start (50)
time.sleep(1)

#stop buzzer 
Buzz. stop ()

#reset resources used by script
GPIO.cleanup()

If GPIO .input(touch_pin) == 0:
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
