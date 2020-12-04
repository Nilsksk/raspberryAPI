import json


def add_new_relay(name: str):
    with open("resources/relays.json", "r") as json_file:
        get_relays = json.load(json_file)

    increase_id = (len(get_relays['relay']) - 1) + 1

    new_data = {"id": increase_id, "name": name}

    get_relays['relay'].append(new_data)

    with open("resources/relays.json", "w") as json_file:
        json.dump(get_relays, json_file, indent=4)


add_new_relay("Zimmer ?")
