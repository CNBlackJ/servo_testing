#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import  os  
import  sys
import  tty, termios
import time    
 

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
    elif ch=='r':
      print 'reset'
    elif ch=='q':
      print 'shutdown'
      break
    elif ord(ch)==0x3:
      print "shutdown"
      break