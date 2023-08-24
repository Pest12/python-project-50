import json


def to_str(value):
    if isinstance(value, str):
        return value
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return value


def generate_diff(file_path1, file_path2):
    diff = []
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    for key in sorted(file1 | file2):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff.append(f'    {key}: {to_str(file1[key])}')
            else:
                diff.append(f'  - {key}: {to_str(file1[key])}\n  + {key}: {to_str(file2[key])}')  # noqa: E501
        elif key in file1 and key not in file2:
            diff.append(f'  - {key}: {to_str(file1[key])}')
        elif key not in file1 and key in file2:
            diff.append(f'  + {key}: {to_str(file2[key])}')
    template = '{\n' + '\n'.join(diff) + '\n}' + '\n'
    return template
