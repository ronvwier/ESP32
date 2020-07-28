from machine import Pin, ADC
from time import sleep
  
class WaterSensor():
    def __init__(self,pin=34):
        self.adc = ADC(Pin(pin, Pin.IN))
        self.adc.width(ADC.WIDTH_12BIT)
    def read(self):
        return self.adc.read()

if __name__ == "__main__":
    ws = WaterSensor(34)
    while True:
      water = ws.read()
      print(water)
      sleep(1)
