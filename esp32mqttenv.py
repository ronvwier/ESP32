import json
import wifi
from umqtt.robust import MQTTClient
from env import Env
import time

#env0 = unit.get(unit.ENV, unit.PORTA)
env0 = Env((21,22))

while True:

    try:
        wifi.check()
        t_temp = env0.temperature
        t_temp = "%.1f"%(t_temp)
        t_press = env0.pressure
        t_press = "%.f"%(t_press)
        t_hum = env0.humidity
        t_hum = "%.f"%(t_hum)
        t_dict = { "temperature": t_temp, 'pressure': t_press, 'humidity': t_hum }
        s_dict = json.dumps(t_dict)

        # publish the message to MQTT
        print("env/out",s_dict)
        c = MQTTClient("esp32mqttenv", "192.168.0.129")
        c.connect()
        c.publish('env/out',s_dict, retain=True, qos=1)
        c.disconnect()
    except:
        print('error')

    time.sleep(20)
