import json
import time
import network

def check():
    nic = network.WLAN(network.STA_IF)
    if not nic.isconnected():
        # enable station interface and connect to WiFi access point
        nic.active(True)
        nic.connect('iot','iot1064wh')
        while not nic.isconnected():
            print('not connected')
            time.sleep(1)
        print(nic.ifconfig())
