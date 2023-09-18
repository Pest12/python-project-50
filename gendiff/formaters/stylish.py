INDENT = 4
ACTION_PREFIX = {
    'same': '    ',
    'added': '  + ',
    'removed': '  - '
}


def stringify(data, depth):
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    elif isinstance(data, str) or isinstance(data, int):
        return data
    lines = ["{"]
    for k, v in data.items():
        lines.append(f"{' ' * depth}{ACTION_PREFIX['same']}{k}: "
                     f"{stringify(v, depth+INDENT)}")
    lines.append(f"{' ' * depth}}}")
    return '\n'.join(lines)


def stringify_diff(diff, depth=0):
    lines = ['{']
    for k, v in diff.items():
        if v['type'] == 'nested_dict':
            new_value = stringify_diff(v['value'], depth + INDENT)
            lines.append(f"{' ' * depth}{ACTION_PREFIX['same']}{k}: "
                         f"{new_value}")
        elif v['type'] == 'updated':
            lines.append(f"{' ' * depth}{ACTION_PREFIX['removed']}{k}: "
                         f"{stringify(v['old_value'], depth+INDENT)}")
            lines.append(f"{' ' * depth}{ACTION_PREFIX['added']}{k}: "
                         f"{stringify(v['new_value'], depth+INDENT)}")
        else:
            lines.append(f"{' ' * depth}{ACTION_PREFIX[v['type']]}{k}: "
                         f"{stringify(v['value'], depth+INDENT)}")
    lines.append(f"{' ' * depth}}}")
    res = '\n'.join(lines)
    return res


def make_stylish(diff):
    return stringify_diff(diff)
