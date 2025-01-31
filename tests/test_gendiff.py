from gendiff.generate_diff_json import generate_diff_json
from gendiff.generate_diff_yaml import generate_diff_yaml


def test_generate_diff_json():
    first_file = "tests/test_data/file1.json"
    second_file = "tests/test_data/file2.json"

    result = generate_diff_json(first_file, second_file)

    expected = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

    assert result == expected


def test_generate_diff_yaml():
    first_file = "tests/test_data/file1.yaml"
    second_file = "tests/test_data/file2.yaml"

    result = generate_diff_yaml(first_file, second_file)

    expected = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

    assert result == expected
