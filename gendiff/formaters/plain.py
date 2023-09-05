def stringify(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        return '[complex value]'
    if isinstance(value, int):
        return str(value)
    return f"'{value}'"


def build(diff, path=""):
    lines = []
    for dictionary in diff:
        name = f"{path}{dictionary['name_key']}"
        if dictionary['type'] == 'added':
            lines.append(f"Property '{name}' was added with value: "
                         f"{stringify(dictionary['new_value'])}")
        elif dictionary['type'] == 'removed':
            lines.append(f"Property '{name}' was removed")
        elif dictionary['type'] == 'updated':
            lines.append(f"Property '{name}' was updated."
                         f" From {stringify(dictionary['old_value'])}"
                         f" to {stringify(dictionary['new_value'])}")
        elif dictionary['type'] == 'nested_dict':
            value = build(dictionary['value'], f"{name}.")
            lines.append(f"{value}")
    return '\n'.join(lines)


def make_plain(dictionary):
    return build(dictionary)
