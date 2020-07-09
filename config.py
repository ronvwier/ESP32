'''
External configuration file reading

Use a config file to store items like your wifi
'''

import json

# proposed format of the JSON file: {"wifi": {"ssid": "your-wifi-name", "passwords": "your-wifi-password"}}
CONFIG_FILE = "config.json"

def cfgRead(part):
    '''Read the config file'''
    global CONFIG_FILE
    
    with open(CONFIG_FILE) as json_file:
        data = json.load(json_file)
        return data[part]
    
# test when run as python file
if __name__ == "__main__":
    print(cfgRead("wifi")['ssid'])
