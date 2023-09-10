def to_str(file):
    for key, val in file.items():
        if isinstance(val, dict):
            to_str(val)
        elif val is None:
            file[key] = 'null'
        elif isinstance(val, bool):
            file[key] = str(file[key]).lower()
    return file
