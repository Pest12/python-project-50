import json


def make_json(dictionary):
    return json.dumps(dictionary, indent=4) + '\n'
