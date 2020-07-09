import json
import time
import network
import config

def check():
    nic = network.WLAN(network.STA_IF)
    if not nic.isconnected():
        # enable station interface and connect to WiFi access point
        cfg = cfgRead("wifi")
        nic.active(True)
        nic.connect(cfg['ssid'],cfg['password'])
        while not nic.isconnected():
            print('not connected')
            time.sleep(1)
        print(nic.ifconfig())
