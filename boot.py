# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import time

print('boot.py start')

# Delay boot for 4 seconds to enable break
for i in range(4):
    print('4 seconds countdown to start')
    time.sleep(1)

# Start the app 
import main
