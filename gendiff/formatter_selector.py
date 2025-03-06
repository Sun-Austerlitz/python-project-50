from typing import Any

from .formatter.format_json import format_json
from .formatter.format_plain import format_plain
from .formatter.format_stylish import format_stylish


def select_formatter(format_name: str) -> Any:
    """
    Selects the appropriate formatter based on the format name.

    Parameters:
        format_name (str): The format type for the output.

    Returns:
        function: The selected formatter function.
    """
    if format_name == "stylish":
        return format_stylish
    elif format_name == "plain":
        return format_plain
    elif format_name == "json":
        return format_json
    else:
        raise ValueError(f"Unsupported format: {format_name}")
