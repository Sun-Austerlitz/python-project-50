from gendiff import generate_diff


def test_generate_diff():
    first_file = "tests/test_data/file1.json"
    second_file = "tests/test_data/file2.json"

    result = generate_diff(first_file, second_file)

    expected = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

    assert result == expected
