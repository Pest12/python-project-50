INDENT = 4
SIGN = {
    'same': '    ',
    'added': '  + ',
    'removed': '  - '
}


def stringify_value(data, depth):
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    elif isinstance(data, str) or isinstance(data, int):
        return data
    lines = ["{"]
    for k, v in data.items():
        lines.append(f"{' ' * depth}    {k}: "
                     f"{stringify_value(v, depth+INDENT)}")
    lines.append(f"{' ' * depth}}}")
    return '\n'.join(lines)


def stringify_diff(diff, depth=0):
    lines = ['{']
    for k, v in diff.items():
        if v['type'] == 'nested_dict':
            new_value = stringify_diff(v['value'], depth+INDENT)
            lines.append(f"{' ' * depth}    {k}: {new_value}")
        elif v['type'] == 'updated':
            lines.append(f"{' ' * depth}  - {k}: "
                         f"{stringify_value(v['old_value'], depth+INDENT)}")
            lines.append(f"{' ' * depth}  + {k}: "
                         f"{stringify_value(v['new_value'], depth+INDENT)}")
        else:
            lines.append(f"{' ' * depth}{SIGN[v['type']]}{k}: "
                         f"{stringify_value(v['value'], depth+INDENT)}")
    lines.append(f"{' ' * depth}}}")
    res = '\n'.join(lines)
    return res


def make_stylish(diff):
    return stringify_diff(diff)
