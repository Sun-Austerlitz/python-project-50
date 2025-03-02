from pathlib import Path

import pytest

from gendiff import generate_diff


def get_test_data_path(filename: str) -> Path:
    """
    Constructs the path to a test data file.

    Parameters:
        filename (str): The name of the test data file.

    Returns:
        Path: The path to the test data file.
    """
    return Path("tests/fixtures") / filename


def read_file(filename: str) -> str:
    """
    Reads the content of a test data file.

    Parameters:
        filename (str): The name of the test data file.

    Returns:
        str: The content of the test data file.
    """
    path = get_test_data_path(filename)
    return path.read_text()


@pytest.mark.parametrize(
    "file1, file2, result_file, format_name",
    [
        ("file1.json", "file2.json", "result.txt", "stylish"),
        ("file1.yaml", "file2.yaml", "result.txt", "stylish"),
        ("file1.json", "file2.json", "result_plain.txt", "plain"),
        ("file1.yaml", "file2.yaml", "result_plain.txt", "plain"),
        ("file1.json", "file2.json", "result_json.txt", "json"),
        ("file1.yaml", "file2.yaml", "result_json.txt", "json"),
    ],
    ids=[
        "json_stylish",
        "yaml_stylish",
        "json_plain",
        "yaml_plain",
        "json_json",
        "yaml_json",
    ],
)
def test_generate_diff(
    file1: str, file2: str, result_file: str, format_name: str
) -> None:
    """
    Tests the generate_diff function for different file formats.

    Parameters:
        file1 (str): The name of the first test data file.
        file2 (str): The name of the second test data file.
        result_file (str): The name of the file containing the expected result.
        format_name (str): The format type for the output.
    """
    file1_path = get_test_data_path(file1)
    file2_path = get_test_data_path(file2)

    expected_result = read_file(result_file)

    diff = generate_diff(file1_path, file2_path, format_name)

    assert expected_result.strip() == diff.strip()
