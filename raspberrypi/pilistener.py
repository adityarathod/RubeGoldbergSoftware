import socket               # Import socket module
import time # Import the time module
import RPi.GPIO as GPIO

serDelay = 0.0015 # The delay between the high and low pulses

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

def move():
   try:
      GPIO.output(7,1)
      time.sleep(serDelay)
      GPIO.output(7,0)
      print "moved."
   except:
      print "Unexpected error:", sys.exc_info()[0]
      move()
      raise
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
   move()
   c.close()                # Close the connection
