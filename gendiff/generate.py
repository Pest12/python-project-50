def build_diff(old, new):
    res = {}
    old_keys = set(old.keys()) - set(new.keys())
    for key in old_keys:
        res[key] = {'type': 'removed', 'value': old[key]}
    new_keys = set(new.keys()) - set(old.keys())
    for key in new_keys:
        res[key] = {'type': 'added', 'value': new[key]}
    for key in old.keys() & new.keys():
        old_val = old[key]
        new_val = new[key]
        if isinstance(old[key], dict) and isinstance(new[key], dict):
            res[key] = {'type': 'nested_dict', 'value': build_diff(old_val, new_val)}
        elif old_val == new_val:
            res[key] = {'type': 'same', 'value': old_val}
        elif old_val != new_val:
            res[key] = {'type': 'updated', 'old_value': old_val, 'new_value': new_val}
    return dict(sorted(res.items(), key=lambda k: k[0]))
