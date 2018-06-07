
import random
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)

random_number = random.randint(1,10)
guess  = int(raw_input("Guess an integer(bewtween 1 and 10): "))
Buzz = GPIO.PWM(buzz_pin, 1000)
Buzz. ChangeFrequency(27.5)
while  random_number != guess :
      Buzz.start (50)
      time.sleep(1)
      Buzz.stop()
      guess  = int(raw_input("Guess an integer(bewtween 1 and 10): "))
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, True)
time.sleep(3)
GPIO.output(led_pin, False)
 
