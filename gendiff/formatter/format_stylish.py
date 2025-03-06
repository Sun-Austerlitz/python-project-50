from typing import Any, Dict, List

from ..constants import (
    FORMAT_INDENT_OFFSET,
    FORMAT_INDENT_SIZE,
    STATUS_ADDED,
    STATUS_CHANGED,
    STATUS_NESTED,
    STATUS_REMOVED,
)


def format_stylish(diff: List[Dict[str, Any]], depth: int = 1) -> str:
    """
    Formats the diff in a stylish format.

    Parameters:
        diff (list): The diff representation.
        depth (int): The current depth for indentation.

    Returns:
        str: The formatted stylish diff.
    """
    indent = " " * (FORMAT_INDENT_SIZE * depth - FORMAT_INDENT_OFFSET)
    lines = []

    for item in diff:
        key = item["key"]
        status = item["status"]
        if status == STATUS_ADDED:
            lines.append(
                f"{indent}+ {key}: {to_str(item['value'], depth + 1)}",
            )
        elif status == STATUS_REMOVED:
            lines.append(
                f"{indent}- {key}: {to_str(item['value'], depth + 1)}",
            )
        elif status == STATUS_CHANGED:
            lines.append(
                f"{indent}- {key}: {to_str(item['old_value'], depth + 1)}",
            )
            lines.append(
                f"{indent}+ {key}: {to_str(item['new_value'], depth + 1)}",
            )
        elif status == STATUS_NESTED:
            lines.append(
                f"{indent}  {key}: {
                    format_stylish(item['children'], depth + 1)}"
            )
        else:  # STATUS_UNCHANGED
            lines.append(
                f"{indent}  {key}: {to_str(item['value'], depth + 1)}",
            )

    closing_indent = " " * (FORMAT_INDENT_SIZE * (depth - 1))
    return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"


def to_str(value: Any, depth: int) -> str:
    """
    Converts a value to its string representation.

    Parameters:
        value: The value to convert.
        depth (int): The current depth for indentation.

    Returns:
        str: The string representation of the value.
    """
    if isinstance(value, dict):
        return format_dict(value, depth)
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_dict(value: Dict[str, Any], depth: int) -> str:
    """
    Formats a dictionary for the stylish output.

    Parameters:
        value (dict): The dictionary to format.
        depth (int): The current depth for indentation.

    Returns:
        str: The formatted dictionary.
    """
    indent = " " * (FORMAT_INDENT_SIZE * depth)
    lines = [f"{indent}{k}: {to_str(v, depth + 1)}" for k, v in value.items()]
    closing_indent = " " * (FORMAT_INDENT_SIZE * (depth - 1))
    return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"
