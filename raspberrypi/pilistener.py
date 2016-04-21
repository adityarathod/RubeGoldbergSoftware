# Import necessary libraries
import urllib2
import RPi.GPIO as GPIO
import time
import sys
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
# A function to cycle through all possible positions for a servo.
def servoT():
    for i in range(3):
        for pos in poslist:
            dcp = pos * 100 / cycleMS
            pwm.start(dcp)
            time.sleep(.5)
# A function to move the servo.
# INPUT FOR FUNCTION: -1 => LEFT; 0 => MIDDLE; 1 => RIGHT
def move(dir):
    pos = middle
    if (dir == -1):
        pos = left
    elif (dir == 1):
        pos = right
    dcp = (pos * 100) / cycleMS
    pwm.start(dcp)
    time.sleep(.5)
print "Welcome to the Rube Goldberg Software!"
pin = raw_input("What Pi connection is this? ")
filen = pin + ".txt"
baseURL = "https://rubedashboard.herokuapp.com/signal/"
while True:
    re = urllib2.urlopen(baseURL+filen).read(100)
    re = re.replace(" ","")
    if re == "GO":
        # Tell the user the good news and move the servo
        print 'Recieved signal.'
        move(1)
        sys.exit(0)
    elif re == "STOP":
        print "No signal yet."
    else:
        print "This is awkward. I can't seem to get the file or the file is messed up.\nThe URL is " + baseURL + filen
    time.sleep(.5)
