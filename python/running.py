# -*- coding: utf-8 -*-
#!/usr/bin/env python    

import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
try:
  while True:
  	for dc in range(0, 50, 5):
  		p.ChangeDutyCycle(dc)
  		time.sleep(0.01)
  	for dc in range(50, -1, -5):
  		p.ChangeDutyCycle(dc)
  		time.sleep(0.01)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()