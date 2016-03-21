import os
print "Wi-Fi Configurator by AppleCrazy\nBEFORE RUNNING THIS APPLICATION, PLUG IN YOUR WI-FI ADAPTER AND REBOOT.\nThis program will reboot your Pi."
ss = raw_input("Network Name (SSID): ")
wipwd = raw_input("Network Key/Password: ")
with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as f:
    f.write("network={\n\tssid=\"" + ss + "\"\n\tpsk=\"" + wipwd + "\"\n}")
print "Wrote configuration to /etc/wpa_supplicant/wpa_supplicant.conf"
print "Restarting network interface..."
os.system("sudo ifdown wlan0")
os.system("sudo ifup wlan0")
print "Rebooting NOW."
os.system("sudo reboot")
