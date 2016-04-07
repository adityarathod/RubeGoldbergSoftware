import os
import sys
import socket
s = socket.socket()
host = "0.0.0.0"
# Need to figure out what port all school networks DON'T block.
port = 0
#ipfile = "~/rubegoldberg/serverip.txt"
ipfile = "~/Desktop/ip.txt"
# DON'T EDIT. Tilde Expansion
ipfile = os.path.expanduser(ipfile)
if os.path.isfile(ipfile):
    try:
        fc = open(ipfile, "r").read().split("\n")
        host = fc[0]
        port = int(fc[1])
    except IOError:
        print "ERROR\n=====\nUnable to open file. The file may have incorrect permissions. Exiting program."
        sys.exit(1)
    except IndexError:
        print "ERROR\n=====\nYour configuration file at\n" + ipfile + "\nis configured incorrectly.\nThe first line of the file must contain the IP address of the next machine, and the second line must have the port number.\nExiting program."
        sys.exit(1)
else:
    print "Config file does not exist, creating one at " + ipfile + "..."
    os.system("touch " + ipfile)
    print "Please edit this file and run this program again. No signal has been sent."
    print "The format of this file is as follows:\n\t-> Line 1: IP address of the next Pi\n\t-> Line 2: Port to connect on"
    sys.exit(0)
print "Rube Goldberg Software, created by AppleCrazy.\nWaiting for keypress..."
raw_input("Press [Enter] to send the signal.")
print "Key pressed. Now sending signal..."
s.connect((host, port))
s.close
print "Signal sent sucessfully."
