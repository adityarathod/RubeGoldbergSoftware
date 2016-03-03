import socket               # Import socket module
import time # Import the time module
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

def move(angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)
s = socket.socket()         # Create a socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Tells the system to okay the reuse of a port
host = socket.gethostname() # Get local machine name
port = 238                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
print "Welcome to the Rube Goldberg Software!\nWaiting for connection on " + host + ":" + str(port) +"..."
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Recieved signal from ', addr
   move(90)
   c.close()                # Close the connection
