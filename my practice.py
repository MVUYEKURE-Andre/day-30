import json
# file="json.json"

try:
    with open("andre.json", "r") as filee:
        data=json.load(filee)
except FileNotFoundError:
    with open("andre.json","w") as fil:
        json.dump("andre.json",fil, indent=5)
finally:
    print("file doesn't exixt")



