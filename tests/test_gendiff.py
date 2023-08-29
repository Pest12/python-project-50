from gendiff import generate_diff
from gendiff.path import get_path
import pytest

@pytest.mark.parametrize(
    "input_file1,input_file2,output_file",
    [
        ("file1.json", "file2.json", "result.txt"),
        ("file1.yaml", "file2.yaml", "result.txt"),
        ("file1-rec.json", "file2-rec.json", "result-rec.txt"),
        ("file1-rec.yaml", "file2-rec.yaml", "result-rec.txt"),
    ]
)
def test_gendiff(input_file1, input_file2, output_file):
    output = get_path(output_file)
    with open(output, encoding='utf8') as result_file:
        result = result_file.read()
        file1 = get_path(input_file1)
        file2 = get_path(input_file2)
        assert generate_diff(file1, file2) == result
