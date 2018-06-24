#!/bin/bash
pid=$(/bin/pidof minicom)
if [ "x" != "x${pid}" ]; then
    killall  minicom
fi
sleep 1
TTY=/dev/ttyUSB0
ampy -p $TTY put $1
