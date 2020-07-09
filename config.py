import json

CONFIG_FILE = "config.json"

def cfgRead(part):
    global CONFIG_FILE
    
    with open(CONFIG_FILE) as json_file:
        data = json.load(json_file)
        return data[part]
    

if __name__ == "__main__":
    print(cfgRead("wifi")['ssid'])
