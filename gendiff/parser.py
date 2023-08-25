import json
import yaml


def parse(file):
    if file.endswith('.json'):
        return json.load(open(file))
    elif file.endswith('yaml') or file.endswith('yml'):
        return yaml.safe_load(open(file))
