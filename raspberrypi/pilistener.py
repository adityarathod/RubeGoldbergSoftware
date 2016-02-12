import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
print ("Welcome to the Rube Goldberg Software!\nWaiting for connection...")
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Recieved signal from ', addr)
   move()
   c.close()                # Close the connection
def move():
   print("Moved.")
