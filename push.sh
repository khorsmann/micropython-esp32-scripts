#!/bin/bash
pid=$(/bin/pidof minicom)
if [ "x" != "x${pid}" ]; then
	killall  minicom
fi

sleep 3
export AMPY_PORT=/dev/ttyUSB0
if [ -f .ttydevice ]; then
    source .ttydevice
fi

ampy put $1
