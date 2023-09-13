from gendiff.parser import get_content
from gendiff.formaters.formater import get_formater
from gendiff.generate import build_diff


def generate_diff(file_path1, file_path2, formater='stylish'):
    parced_data1 = get_content(file_path1)
    parced_data2 = get_content(file_path2)
    diff = build_diff(parced_data1, parced_data2)
    return get_formater(diff, formater)
