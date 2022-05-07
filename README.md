
# install adafruit ampy for up/download via ttyUSB

pip3 install --user adafruit-ampy

# find the correct ttyUSB device

```shell
sudo dmesg | grep cp210x

[340114.819104] usbcore: registered new interface driver cp210x
[340114.819147] usbserial: USB Serial support registered for cp210x
[340114.819269] cp210x 1-1.3:1.0: cp210x converter detected
[340114.827283] usb 1-1.3: cp210x converter now attached to ttyUSB3
```

# check permissions of the ttyUSB device

```shell
ls -lah /dev/ttyUSB0
crw-rw---- 1 root dialout 188, 0 Mai  7 13:17 /dev/ttyUSB0
```

# add user to group

On Debian/Ubuntu:
```shell
adduser <youruser> dialout
```

# push.sh

./push.sh main.py

# esptool.py for flashing micropython to esp

```shell
pip install --user esptool
```

## show flash\_id

```shell
esptool.py -p /dev/ttyUSB0 flash_id 
esptool.py v3.3
Serial port /dev/ttyUSB0
Connecting....
Detecting chip type... Unsupported detection protocol, switching and trying again...
Connecting.......
Detecting chip type... ESP32
Chip is ESP32-D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, Coding Scheme None
Crystal is 40MHz
MAC: 30:ae:XX:XX:XX:XX
Uploading stub...
Running stub...
Stub running...
Manufacturer: c8
Device: 4016
Detected flash size: 4MB
Hard resetting via RTS pin...
```
