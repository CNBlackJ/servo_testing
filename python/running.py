# -*- coding: utf-8 -*-
#!/usr/bin/env python    

import RPi.GPIO as GPIO
import time
import sys
import tty, termios

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

minAngle = sys.argv[1] if sys.argv[1] else 40
maxAngle = sys.argv[2] if sys.argv[2] else 90

minDc = (45 + int(minAngle)) / 18
maxDc = (45 + int(maxAngle)) / 18

if __name__ == '__main__':
  print "Reading from keybord..."
  print "d: drop; r: reset; q to qiut;"
  while True:
    fd=sys.stdin.fileno()
    old_settings=termios.tcgetattr(fd)
    try:
      tty.setraw(fd)
      ch=sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch=='d':
      print 'drop'
      drop()
    elif ch=='r':
      print 'reset'
      reset()
    elif ch=='q':
      print 'shutdown'
      break
    elif ord(ch)==0x3:
      print "shutdown"
      break

def drop():
  try:
    p1.ChangeDutyCycle(maxDc)
    p2.ChangeDutyCycle(maxDc)
    p3.ChangeDutyCycle(maxDc)
    time.sleep(0.5) # sleep 0.5 second
    p1.ChangeDutyCycle(minDc)
    p2.ChangeDutyCycle(minDc)
    p3.ChangeDutyCycle(minDc)
    time.sleep(0.5) # sleep 0.5 second 
  finally:
    print("clean up")
    GPIO.cleanup() # cleanup all GPIO

def reset():
  try:
    p1.ChangeDutyCycle(90)
    p2.ChangeDutyCycle(90)
    p3.ChangeDutyCycle(90)
    time.sleep(0.5) # sleep 0.5 second
  finally:
    print("clean up")
    GPIO.cleanup() # cleanup all GPIO