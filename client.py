import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "10.20.22.22"     # Hard coded to my 101A machine.
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print (s.recv(1024).decode())
s.close                     # Close the socket when done
