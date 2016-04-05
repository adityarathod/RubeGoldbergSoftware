import os
import subprocess
def shell(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0].rstrip('\n')
print "Wi-Fi Configurator 0.1.0 by AppleCrazy\nBEFORE RUNNING THIS APPLICATION, PLUG IN YOUR WI-FI ADAPTER AND REBOOT.\nEXIT THIS PROGRAM BY PRESSING CONTROL-C.\nThis program WILL reboot your Pi.\nAlso, do not reconfigure Wi-Fi settings through this utility- this will DAMAGE the CONFIG FILE."
print "[Step 1] Select an SSID from the following list: "
print "Type it in EXACTLY as you see below, but without quotes."
# print "ESSID:\"Hello\"".replace("ESSID:", "=>\t") # For testing!!
print shell("sudo iwlist wlan0 scan | grep ESSID").replace("ESSID:", "=>\t")
ss = raw_input("Network Name (SSID): ")
print "[Step 2] Enter the PASSWORD for the network. \nThis is case sensitive and will be shown in plaintext onscreen."
wipwd = raw_input("Network Key/Password: ")
with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as f:
    f.write("network={\n\tssid=\"" + ss + "\"\n\tpsk=\"" + wipwd + "\"\n\tkey_mgmt=WPA-PSK\n}")
print "Wrote configuration to /etc/wpa_supplicant/wpa_supplicant.conf"
print "Rebooting NOW. Please wait..."
shell("sudo reboot")
