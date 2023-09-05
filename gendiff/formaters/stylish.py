START_INDENT = 2


def to_str(value, depth):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        return build_result(value, depth + START_INDENT)
    return value


def forming_a_string(dictionary, key, depth, sign):
    return f"{' ' * depth}{sign}{dictionary['name_key']}: " \
           f"{to_str(dictionary[key], depth + START_INDENT)}"


def build_result(dictionary, depth=0):
    final = ['{']
    for key in dictionary:
        if key['type'] == 'not updated' or key['type'] == 'nested':
            final.append(forming_a_string(
                          key, 'value', depth, sign='    '))
        elif key['type'] == 'updated':
            final.append(forming_a_string(
                          key, 'old_value', depth, sign='  - '))
            final.append(forming_a_string(
                          key, 'new_value', depth, sign='  + '))
        elif key['type'] == 'removed':
            final.append(forming_a_string(
                          key, 'old_value', depth, sign='  - '))
        elif key['type'] == 'added':
            final.append(forming_a_string(
                          key, 'new_value', depth, sign='  + '))
    final.append(f'{" " * depth}}}')
    return '\n'.join(final)


def make_stylish(dictionary):
    return build_result(dictionary)
