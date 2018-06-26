
# install adafruit ampy for up/download via ttyUSB

sudo pip3 install adafruit-ampy

# find the correct ttyUSB device

sudo dmesg | grep cp210x

[340114.819104] usbcore: registered new interface driver cp210x
[340114.819147] usbserial: USB Serial support registered for cp210x
[340114.819269] cp210x 1-1.3:1.0: cp210x converter detected
[340114.827283] usb 1-1.3: cp210x converter now attached to ttyUSB3

# push.sh

./push.sh main.py

