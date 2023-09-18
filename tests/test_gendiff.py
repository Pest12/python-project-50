from tests.conftest import get_fixture_path
from gendiff import generate_diff
import pytest


@pytest.mark.parametrize(
    "input_file1,input_file2,output_file,formater",
    [
        ("file1.json", "file2.json", "result.txt", 'stylish'),
        ("file1.json", "file2.json", "result.txt", None),
        ("file1.yaml", "file2.yaml", "result.txt", 'stylish'),
        ("file1.yaml", "file2.yaml", "result.txt", None),
        ("file1-rec.json", "file2-rec.json", "result-rec.txt", 'stylish'),
        ("file1-rec.json", "file2-rec.json", "result-rec.txt", None),
        ("file1-rec.yaml", "file2-rec.yaml", "result-rec.txt", 'stylish'),
        ("file1-rec.yaml", "file2-rec.yaml", "result-rec.txt", None),
        ("file1-rec.json", "file2-rec.json", "result-plain.txt", 'plain'),
        ("file1-rec.yaml", "file2-rec.yaml", "result-plain.txt", 'plain'),
        ("file1.json", "file2.json", "result-json.txt", 'json'),
        ("file1.yaml", "file2.yaml", "result-json.txt", 'json'),
    ]
)
def test_gendiff(input_file1, input_file2, output_file, formater):
    output = get_fixture_path(output_file)
    with open(output) as result_file:
        result = result_file.read()
        file1 = get_fixture_path(input_file1)
        file2 = get_fixture_path(input_file2)
        assert generate_diff(file1, file2, formater) == result[:-1]
