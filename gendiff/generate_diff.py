from gendiff.parser import parse
from gendiff.formaters.formater import get_formater
from gendiff.generate import build_diff


def generate_diff(file_path1, file_path2, formater='stylish'):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    diff = build_diff(file1, file2)
    return get_formater(diff, formater)
