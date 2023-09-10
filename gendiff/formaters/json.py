from gendiff.formaters.stylish import to_str
import json


def make_json(dictionary):
    diff = to_str(dictionary)
    return json.dumps(diff, indent=4)
