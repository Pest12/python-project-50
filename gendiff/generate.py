from collections import OrderedDict


def build_diff(old, new):
    res = {}
    keys = set(new.keys()) | set(old.keys())
    for key in keys:
        if key not in new:
            res[key] = {'type': 'removed', 'value': old[key]}
        elif key not in old:
            res[key] = {'type': 'added', 'value': new[key]}
        elif isinstance(old[key], dict) and isinstance(new[key], dict):
            res[key] = {
                'type': 'nested_dict', 'value': build_diff(old[key], new[key])
            }
        elif old[key] != new[key]:
            res[key] = {
                'type': 'updated', 'old_value': old[key],
                'new_value': new[key]
            }
        elif old[key] == new[key]:
            res[key] = {'type': 'same', 'value': old[key]}
    return OrderedDict(sorted(res.items()))
