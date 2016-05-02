#!/usr/bin/env python
import time
import os
n = ""
with open("/home/pi/pinum.txt","read") as f:
    n = f.read()
for i in range(59):
    os.system("curl --data \"id=" + n + "\" https://rubedashboard.herokuapp.com/pistate.php")
    print "iteration " + str(i)
    time.sleep(0.8)
