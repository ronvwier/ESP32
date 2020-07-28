from time import sleep
from water import WaterSensor
  
ws = WaterSensor(34)
while True:
  water = ws.read()
  print(water)
  sleep(1)
  