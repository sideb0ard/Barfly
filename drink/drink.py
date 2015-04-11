#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time
import sys

# init GPIO
GPIO.setup("P8_7", GPIO.IN)
GPIO.setup("P8_8", GPIO.OUT)

# turn pump on via relay
GPIO.output("P8_8", GPIO.LOW)

# listen for sample aquired signal
while True:
  if GPIO.input("P8_7"):
    # cut power to pump and exit
    print "derp"
    GPIO.output("P8_8", GPIO.HIGH)
    sys.exit(0)
  time.sleep(.01)

