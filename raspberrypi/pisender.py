import os

import socket
s = socket.socket()
# Localhost for testing purposes, please replace "socket.gethostname()" with the IP address of the next school, in quotes.
host = socket.gethostname() #"127.0.0.1"
# Need to figure out what port all school networks DON'T block.
port = 238
print "Welcome to the Rube Goldberg Software, created by AppleCrazy.\nWaiting for keypress..."
raw_input("Press [Enter] to send the signal.")
print "Key pressed. Now sending signal..."
s.connect((host, port))
s.close
print "Signal sent sucessfully."
