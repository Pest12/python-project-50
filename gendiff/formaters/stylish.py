SIGN = {
    'same': '  ',
    'added': '+ ',
    'removed': '- '
}


def to_str(file):
    for key, val in file.items():
        if isinstance(val, dict):
            to_str(val)
        elif val is None:
            file[key] = 'null'
        elif isinstance(val, bool):
            file[key] = str(file[key]).lower()
    return file


def stringify_value(data, depth):
    if not isinstance(data, dict):
        return data
    lines = ["{"]
    for k, v in data.items():
        lines.append(f"{'  '*depth}  {k}: {stringify_value(v, depth+2)}")
    lines.append(f"{'  '*(depth-1)}}}")
    return '\n'.join(lines)


def stringify_diff(diff, depth=1):
    lines = []
    for k, v in diff.items():
        if v['type'] == 'nested_dict':
            lines.append(f"{'  ' * depth}  {k}: {{")
            lines.append(f"{stringify_diff(v['value'], depth+2)}")
            lines.append(f"{'  ' * (depth+1)}}}")
        elif v['type'] == 'updated':
            lines.append(f"{'  ' * depth}- {k}: "
                         f"{stringify_value(v['old_value'], depth+2)}")
            lines.append(f"{'  ' * depth}+ {k}: "
                         f"{stringify_value(v['new_value'], depth+2)}")
        else:
            lines.append(f"{'  ' * depth}{SIGN[v['type']]}{k}: "
                         f"{stringify_value(v['value'], depth+2)}")
    res = '\n'.join(lines)
    return res


def make_stylish(diff):
    diff = to_str(diff)
    return f"{{\n{stringify_diff(diff)}\n}}"
