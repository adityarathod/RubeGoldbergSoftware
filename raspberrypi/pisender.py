import os
import sys
base = "curl --data \"to="
tail = "\" https://rubedashboard.herokuapp.com/signal/send.php"
print "Rube Goldberg Software, created by AppleCrazy."
numcon = raw_input("Pi Connection ID: ")
cmd = base + numcon + tail
print "Waiting for keypress..."
raw_input("Press [Enter] to send the signal.")
print "Key pressed. Now sending signal..."
os.system(cmd)
