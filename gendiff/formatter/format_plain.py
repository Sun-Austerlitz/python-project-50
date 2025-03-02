from typing import Any, Dict, List


def format_plain(diff: Dict[str, Any], parent_key: str = "") -> str:
    """
    Formats the diff in a plain format.

    Parameters:
        diff (dict): The diff representation.
        parent_key (str): The parent key for nested properties.

    Returns:
        str: The formatted plain diff.
    """
    lines = _format_diff(diff, parent_key)
    return "\n".join(lines)


def _format_diff(diff: Dict[str, Any], parent_key: str) -> List[str]:
    """
    Recursively formats the diff into a list of plain text lines.

    Parameters:
        diff (dict): The diff representation.
        parent_key (str): The parent key for nested properties.

    Returns:
        List[str]: The list of formatted plain text lines.
    """
    lines = []
    for key, value in diff.items():
        current_key = f"{parent_key}.{key}" if parent_key else key
        status = value.get("status")

        if status == "added":
            lines.append(
                f"Property '{current_key}' was added with value: {
                    format_value(value['value'])}"
            )
        elif status == "removed":
            lines.append(f"Property '{current_key}' was removed")
        elif status == "changed":
            old_value = format_value(value["old_value"])
            new_value = format_value(value["new_value"])
            lines.append(
                f"Property '{
                    current_key}' was updated. From {old_value} to {new_value}"
            )
        elif status == "nested":
            lines.extend(_format_diff(value["children"], current_key))

    return lines


def format_value(value: Any) -> str:
    """
    Formats a value for the plain output.

    Parameters:
        value: The value to format.

    Returns:
        str: The formatted value.
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
