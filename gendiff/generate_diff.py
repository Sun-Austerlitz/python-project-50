from .core import get_file_format, parse_data, read_file
from .diff_builder import build_diff
from .formatter_selector import select_formatter


def generate_diff(file1: str, file2: str, format_name: str = "stylish") -> str:
    """
    Generates a diff between two files and formats it.

    Parameters:
        file1 (str): The path to the first file.
        file2 (str): The path to the second file.
        format_name (str): The format type for the output.

    Returns:
        str: The formatted diff.
    """
    data1 = parse_data(read_file(file1), get_file_format(file1))
    data2 = parse_data(read_file(file2), get_file_format(file2))
    diff = build_diff(data1, data2)
    return select_formatter(diff, format_name)
