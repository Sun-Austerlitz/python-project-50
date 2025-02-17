import pytest
from gendiff.generate_diff import generate_diff


# Fixture for preparing JSON files
@pytest.fixture
def json_files():
    return "tests/fixtures/file1.json", "tests/fixtures/file2.json"


# Fixture for preparing YAML files
@pytest.fixture
def yaml_files():
    return "tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml"


# Parameterized test for different file formats
@pytest.mark.parametrize(
    "file_type, files",
    [
        ("json", pytest.lazy_fixture("json_files")),
        ("yaml", pytest.lazy_fixture("yaml_files")),
    ],
)
def test_generate_diff(file_type, files):
    """
    Test the generate_diff function for different file formats.
    """
    first_file, second_file = files

    expected_output = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

    result = generate_diff(first_file, second_file)
    assert result == expected_output


# Test for unsupported file format
def test_generate_diff_unsupported_format():
    """
    Test the generate_diff function with an unsupported file format.
    """
    with pytest.raises(
        ValueError, match="Unsupported file format or mismatched file formats"
    ):
        generate_diff("tests/fixtures/file1.txt", "tests/fixtures/file2.txt")


# Test for mismatched file formats
def test_generate_diff_mismatched_formats():
    """
    Test the generate_diff function with mismatched file formats.
    """
    with pytest.raises(
        ValueError, match="Unsupported file format or mismatched file formats"
    ):
        generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.yaml")
