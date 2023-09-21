def stringify(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, int):
        return str(value)
    return f"'{value}'"


def build(diff, path=""):
    lines = []
    for k, v in diff.items():
        property_path = f"{path}{k}"
        if v['type'] == 'added':
            lines.append(f"Property '{property_path}' was added with value: "
                         f"{stringify(v['value'])}")
        elif v['type'] == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif v['type'] == 'updated':
            lines.append(f"Property '{property_path}' was updated."
                         f" From {stringify(v['old_value'])}"
                         f" to {stringify(v['new_value'])}")
        elif v['type'] == 'nested_dict':
            value = build(v['value'], f"{property_path}.")
            lines.append(f"{value}")
    return '\n'.join(lines)


def to_plain(diff):
    return build(diff)
