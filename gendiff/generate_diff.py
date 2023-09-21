from gendiff.parser import get_content
from gendiff.formaters.formater import get_formater
from gendiff.generate import build_diff


def generate_diff(file_path1, file_path2, formater='stylish'):
    content1 = get_content(file_path1)
    content2 = get_content(file_path2)
    dicts_diff = build_diff(content1, content2)
    return get_formater(dicts_diff, formater)