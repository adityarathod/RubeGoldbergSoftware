# Import necessary libraries
import RPi.GPIO as GPIO
import time
# This is programmatic GPIO port 18, but physical pin 12.
# For more details on this, see the README.
controlPort = 18
# This configures the GPIO library to use programmatic ports.
# GPIO.BOARD as a function argument allows you to pass in physical pin numbers.
GPIO.setmode(GPIO.BCM)
# Get some stuff set up
GPIO.setup(controlPort,GPIO.OUT)
# The cycle frequency (in Hz)
cycleFreq = 50
# Set up a PWM reference so we can call it later
pwm = GPIO.PWM(controlPort,cycleFreq)
# Duty cycle constants
left = 0.75
right = 2.5
middle = (right - left) / 2 + left
# End constants
# The "moves" that the servo can make
poslist = [left,middle,right,middle]
# The time (in ms) per cycle
cycleMS = 1000 / cycleFreq
# A function to move the servo.
# INPUT FOR FUNCTION: -1 => RIGHT; 0 => MIDDLE; 1 => LEFT
def move(dir):
    pos = middle
    if (dir == -1):
        pos = left
    elif (dir == 1):
        pos = right
    dcp = (pos * 100) / cycleMS
    pwm.start(dcp)
    time.sleep(.5)

while True:
  print "Moving right"
  move(-1)
  print "Moving left"
  move(1)
  print "Moving to the middle"
  move(0)
