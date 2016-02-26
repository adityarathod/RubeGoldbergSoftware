# Rube Goldberg Software
##### Raspberry Pi 

![current version](https://img.shields.io/badge/current%20version-0.2.0__37-brightgreen.svg)

##### Windows 

![retired](https://img.shields.io/badge/current%20version-retired-red.svg)

**PLEASE KEEP YOUR SOFTWARE UP TO DATE.**

Triggers for Rube Goldberg machines.

Visit us on [berbawy.com](http://berbawy.com/makers).


## How to Use the Preconfigured Pis
If you have a Raspberry Pi with the preconfigured image, you have all the necessary software and modifications to keep your Pi up to date and ready to use.
### Commands You Can Use
| Command |            Function           |
|---------|-------------------------------|
| `rgupdate` | Run the software updater manually, already runs at boot. **Note:** Before running ANY tests, make sure you run this command. |
| `rgversion` | Display the version of the software. This will come in handy when dealing with software issues (if any).|
| `pisender` | Run the pisender Python script located at `/home/pi/rubegoldberg/raspberrypi/pisender.py`. **ALWAYS** run the sender from here. |
| `pilistener` | Run the pisender Python script located at `/home/pi/rubegoldberg/raspberrypi/pilistener.py`. **ALWAYS** run the listener from here. |
### Can I install my own software/games on these systems?
It is not recommended to install any other applications on these images as they may interfere with the network port availability or cause other unforseen changes to the system.
### Can I change any settings?
It is not recommended to change any other setting other than the Wi-Fi settings (connecting the Pi to a Wi-Fi network).
### What should I plug into the Pi?
Please plug in a USB Wi-Fi dongle, a USB keyboard, and a display (preferrably through HDMI).
### Why do these systems boot up to a command prompt?
They are configured as such. Most of the time, this is all that you will need. However, if you are more confortable with a standard Windows or Mac-style interface, just type in `startx` at the command prompt.
**Note:** You cannot run the software from this interface. You must use the command prompt.
### How do I shut down the Pis?
Type in `sudo shutdown now` and give it a minute. Once your screen goes blank, you can unplug all I/O and power.
