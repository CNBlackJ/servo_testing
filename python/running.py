# -*- coding: utf-8 -*-
#!/usr/bin/env python    

import RPi.GPIO as GPIO
import time

servoPIN1 = 17
servoPIN2 = 27
servoPIN3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
GPIO.setup(servoPIN3, GPIO.OUT)

p1 = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p2 = GPIO.PWM(servoPIN, 50)
p3 = GPIO.PWM(servoPIN, 50)
p1.start(0) # Initialization
p2.start(0)
p3.start(0)
try:
  while True:
    # p.ChangeDutyCycle(7.5)  # turn towards 90 degree
    # time.sleep(1) # sleep 1 second
    p1.ChangeDutyCycle(2.5)  # turn towards 0 degree
    p2.ChangeDutyCycle(2.5)
    p3.ChangeDutyCycle(2.5)
    time.sleep(0.5) # sleep 1 second
    p1.ChangeDutyCycle(12.5) # turn towards 180 degree
    p2.ChangeDutyCycle(12.5)
    p3.ChangeDutyCycle(12.5)
    time.sleep(0.5) # sleep 1 second 
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()