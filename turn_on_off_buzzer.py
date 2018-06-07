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
Buzz = GPIO. PWM(buzz_pin, 1000)
Buzz.ChangeFrequency(550)

#change frequency and start passive buzzer using buzz function with 50% duty for 1 second
Buzz.start (50)
time.sleep(1)

#stop buzzer 
Buzz. stop ()

#reset resources used by script
GPIO.cleanup()
