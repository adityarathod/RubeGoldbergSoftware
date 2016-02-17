import os
import socket
s = socket.socket()
# Localhost for testing purposes
host = "127.0.0.1"
# Need to figure out what port all school networks DON'T block.
port = 12345
print "Welcome to the Rube Goldberg Software!\nWaiting for keypress..."
os.system("pause")
print "Key pressed. Now sending signal..."
s.connect((host, port))
s.close
