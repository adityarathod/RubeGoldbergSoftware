# Import necessary libraries
import socket
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
# Create a socket object
s = socket.socket()
# Set up the socket object so that reusing a port is okay
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Get the local hostname
host = socket.gethostname()
# Port to request the OS to reserve a port
port = 238
# Bind to the port
s.bind((host, port))
# Now it's a waiting game.
s.listen(5)
print "Welcome to the Rube Goldberg Software!\nWaiting for connection on " + host + ":" + str(port) +"..."
while True:
    # Got a connection? Great! Accept it.
    c, addr = s.accept()
    # Tell the user the good news and move the servo
    print 'Recieved signal from ', addr
    move(1)
    # Bye.
    c.close()
