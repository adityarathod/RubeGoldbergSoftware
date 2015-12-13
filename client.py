import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "127.0.0.1"         # IPs need to be hard-coded because of the issue with school networks.
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print (s.recv(1024).decode())
s.close                     # Close the socket when done
