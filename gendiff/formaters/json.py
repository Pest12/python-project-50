from gendiff.formaters.correct_keys import to_str
import json


def make_json(dictionary):
    diff = to_str(dictionary)
    return json.dumps(diff, indent=4)
