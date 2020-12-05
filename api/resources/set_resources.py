import json


def add_new_relay(name: str, relay_num: int, state: str = "off"):
    with open("api/resources/relays.json", "r") as json_file:
        get_relays = json.load(json_file)

    increase_id = (len(get_relays) - 1) + 1

    if state == '':
        state = "off"

    new_data = {"id": increase_id, "name": name, "relay_number": relay_num, "state": state}

    get_relays.append(new_data)

    with open("api/resources/relays.json", "w") as json_file:
        json.dump(get_relays, json_file, indent=4)


def update_relay(data: dict):
    with open("api/resources/relays.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
