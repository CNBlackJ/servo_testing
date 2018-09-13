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

p1 = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
p2 = GPIO.PWM(servoPIN2, 50)
p3 = GPIO.PWM(servoPIN3, 50)
p1.start(0) # Initialization
p2.start(0)
p3.start(0)
try:
  while True:
    # p.ChangeDutyCycle(7.5)  # turn towards 90 degree
    # time.sleep(1) # sleep 1 second
    p1.ChangeDutyCycle(8.5)  # turn towards 0 degree
    p2.ChangeDutyCycle(8.5)
    p3.ChangeDutyCycle(8.5)
    time.sleep(0.5) # sleep 1 second
    p1.ChangeDutyCycle(4.5) # turn towards 180 degree
    p2.ChangeDutyCycle(4.5)
    p3.ChangeDutyCycle(4.5)
    time.sleep(0.5) # sleep 1 second 
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
finally:
   print("clean up") 
   GPIO.cleanup() # cleanup all GPIO 