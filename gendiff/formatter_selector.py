from typing import Any, Dict, List

from .formatter.format_json import format_json
from .formatter.format_plain import format_plain
from .formatter.format_stylish import format_stylish


def select_formatter(diff: List[Dict[str, Any]], format_name: str) -> str:
    """
    Selects the appropriate formatter
    based on the format name and returns the formatted diff.

    Parameters:
        diff (list): The diff representation.
        format_name (str): The format type for the output.

    Returns:
        str: The formatted diff.
    """
    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    elif format_name == "json":
        return format_json(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
