import json
import yaml
import os


def get_content(path):
    _, extension = os.path.splitext(path)
    with open(path) as content:
        data = content.read()
        return parse(data, extension[1:])


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)
    if extension == 'yaml' or extension == 'yml':
        return yaml.safe_load(data)
    raise ValueError('Unrecognized extension')
