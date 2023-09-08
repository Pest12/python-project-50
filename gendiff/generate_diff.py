from gendiff.parser import parse
from gendiff.parser import get_content
from gendiff.formaters.formater import get_formater
from gendiff.generate import build_diff


def generate_diff(file_path1, file_path2, formater='stylish'):
    file1, extension1 = get_content(file_path1)
    file2, extension2 = get_content(file_path2)
    parced_data1 = parse(file1, extension1)
    parced_data2 = parse(file2, extension2)
    diff = build_diff(parced_data1, parced_data2)
    return get_formater(diff, formater)
