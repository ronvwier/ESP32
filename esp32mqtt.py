import json
import wifi
import machine
import time
from umqtt.robust import MQTTClient

while True:

    # connect to WiFi
    wifi.check()
    msg = "ESP32 micropython 1.12"
    t_dict = { "ticks": time.ticks_ms(), 'msg': msg }
    s_dict = json.dumps(t_dict)
    print(s_dict)

    # publish the message to MQTT
    c = MQTTClient("esp32mqtt", "192.168.0.129")
    c.connect()
    c.publish('timer/ticks',s_dict, retain=False, qos=1)
    c.disconnect()
        
    time.sleep(20)

