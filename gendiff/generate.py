def build_diff(old, new):  # noqa: C901
    res = {}
    deleted = set(old.keys()) - set(new.keys())
    added = set(new.keys()) - set(old.keys())
    keys = set(new.keys()) | set(old.keys())
    for key in keys:
        if key in deleted:
            res[key] = {'type': 'removed', 'value': old[key]}
        if key in added:
            res[key] = {'type': 'added', 'value': new[key]}
        if key in old and key in new:
            old_val = old[key]
            new_val = new[key]
            if isinstance(old_val, dict) and isinstance(new_val, dict):
                res[key] = {
                    'type': 'nested_dict', 'value': build_diff(old_val, new_val)
                }
            elif old_val != new_val:
                res[key] = {
                   'type': 'updated', 'old_value': old_val, 'new_value': new_val
                }
            else:
                res[key] = {'type': 'same', 'value': old_val}
    return dict(sorted(res.items(), key=lambda k: k[0]))
