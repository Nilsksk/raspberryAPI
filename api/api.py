import json

with open("resources/relays.json", "r") as json_file:
    get_relays = json.load(json_file)


print(get_relays)

x = {"id": 4, "name": "Zimmer 5"}

get_relays['relay'].append(x)

print(get_relays)

with open("resources/relays.json", "w") as json_file:
    json.dump(get_relays, json_file, indent=4)