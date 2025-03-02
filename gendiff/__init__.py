from .core import build_diff, read_file
from .formatter.format_json import format_json
from .formatter.format_plain import format_plain
from .formatter.format_stylish import format_stylish


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
    data1 = read_file(file1)
    data2 = read_file(file2)
    diff = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
