import socket

s = socket.socket()
# Localhost for testing purposes
host = "127.0.0.1"
# Need to figure out what port all school networks DON'T block.
port = 12345

s.connect((host, port))
print (s.recv(1024).decode())
s.close
