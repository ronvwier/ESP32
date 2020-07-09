from machine import Pin, I2C

#i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x5C)


print('esp32_i2c_scan: start')

print('esp32_i2c_scan: construct a software I2C bus')
i2c = I2C(scl=Pin(21), sda=Pin(22), freq=100000)

#print('construct a hardware I2C bus')
#i2c = I2C(0)
#i2c = I2C(1, scl=Pin(21), sda=Pin(22), freq=400000)

print('esp32_i2c_scan: scan i2c bus')
lijst = i2c.scan()

print('esp32_i2c_scan: print list')
print(lijst)
