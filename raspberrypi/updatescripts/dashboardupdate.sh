#!/bin/bash
echo "Rube Software Update 1.1.0_86"
echo "Creating log file at ~/commslog.txt ..."
touch /home/pi/commslog.txt
touch /home/pi/pinum.txt
echo "Adding script to cron (task scheduler)...please wait."
(crontab -l 2>/dev/null; echo "* * * * * python /home/pi/rubegoldberg/RubeGoldbergSoftware/raspberrypi/dashboardcomms.py >> /home/pi/commslog.txt 2>&1") | crontab -
echo "Sucessfully updated."
