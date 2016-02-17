import socket               # Import socket module

def move():
   print "moved."
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
