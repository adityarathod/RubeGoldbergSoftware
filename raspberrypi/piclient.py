import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
s = socket.socket()
# Localhost for testing purposes
host = "127.0.0.1"
# Need to figure out what port all school networks DON'T block.
port = 12345

s.connect((host, port))
if (s.recv(1024).decode()) == "GO":
  servo()
s.close
