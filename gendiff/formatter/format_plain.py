from typing import Any, Dict, List

from ..constants import (
    STATUS_ADDED,
    STATUS_CHANGED,
    STATUS_NESTED,
    STATUS_REMOVED,
)


def format_plain(diff: List[Dict[str, Any]], parent_key: str = "") -> str:
    """
    Formats the diff in a plain format.

    Parameters:
        diff (list): The diff representation.
        parent_key (str): The parent key for nested properties.

    Returns:
        str: The formatted plain diff.
    """
    lines = _format_diff(diff, parent_key)
    return "\n".join(lines)


def _format_diff(diff: List[Dict[str, Any]], parent_key: str) -> List[str]:
    """
    Recursively formats the diff into a list of plain text lines.

    Parameters:
        diff (list): The diff representation.
        parent_key (str): The parent key for nested properties.

    Returns:
        List[str]: The list of formatted plain text lines.
    """
    lines = []
    for item in diff:
        key = item["key"]
        current_key = f"{parent_key}.{key}" if parent_key else key
        status = item["status"]

        if status == STATUS_ADDED:
            lines.append(
                f"Property '{current_key}' was added with value: {
                    to_str(item['value'])}"
            )
        elif status == STATUS_REMOVED:
            lines.append(f"Property '{current_key}' was removed")
        elif status == STATUS_CHANGED:
            old_value = to_str(item["old_value"])
            new_value = to_str(item["new_value"])
            lines.append(
                f"Property '{current_key}' was updated. "
                f"From {old_value} to {new_value}"
            )
        elif status == STATUS_NESTED:
            lines.extend(_format_diff(item["children"], current_key))

    return lines


def to_str(value: Any) -> str:
    """
    Converts a value to its string representation.

    Parameters:
        value: The value to convert.

    Returns:
        str: The string representation of the value.
    """
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return "[complex value]"
