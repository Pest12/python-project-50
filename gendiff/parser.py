import json
import yaml
import os


def get_content(path):
    extension = os.path.splitext(path)[1]
    with open(path) as content:
        data = content.read()
        return data, extension


def parse(file_data, extension):
    if extension == '.json':
        return json.loads(file_data)
    if extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(file_data)
    raise ValueError('Unrecognized extension')
