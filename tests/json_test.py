from gendiff import generate_diff
import json


def test_json():
    result_file = 'tests/fixtures/result.txt'
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    with open(result_file, encoding='utf8') as result:
        assert generate_diff(file1, file2) == result.read()
