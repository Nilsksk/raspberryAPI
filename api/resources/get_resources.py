import json


def get_all_relays() -> dict:
    with open("resources/relays.json", "r") as json_file:
        get_relays = json.load(json_file)

    return get_relays
