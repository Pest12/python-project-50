from gendiff.formaters.correct_keys import to_str


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
            if v['type'] == 'same':
                lines.append(f"{'  ' * depth}  {k}: "
                          f"{stringify_value(v['value'], depth+2)}")
            elif v['type'] == 'added':
                lines.append(f"{'  ' * depth}+ {k}: "
                          f"{stringify_value(v['value'], depth+2)}")
            elif v['type'] == 'removed':
                lines.append(f"{'  ' * depth}- {k}: "
                          f"{stringify_value(v['value'], depth+2)}")
    res = '\n'.join(lines)
    return res


def make_stylish(diff):
    diff = to_str(diff)
    return f"{{\n{stringify_diff(diff)}\n}}"
