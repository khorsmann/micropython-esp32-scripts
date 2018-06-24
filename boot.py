# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

def start_webrepl():
    import webrepl
    webrepl.start()

def read_config():
    import json
    with open('config.json', 'r')  as f:
        cfg = json.load(f)
    return cfg

def connect(essid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)


cfg = read_config()

# debug on/off
if cfg['os']['debug'] is False:
    no_debug()

# network an webrepl - ws port 8266
if cfg['network']['enable']:
    print('configure network')
    connect(cfg['network']['essid'], cfg['network']['password'])
    if cfg['webrepl']['enable']:
        print('try to start webrepl on ws://0.0.0.0:8266/')
        start_webrepl()
else:
    print('config.json network not enabled')
