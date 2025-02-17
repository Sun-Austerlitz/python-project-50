from typing import Any, Dict

FORMAT_INDENT_SIZE = 4
FORMAT_INDENT_OFFSET = 2

STATUS_ADDED = "added"
STATUS_REMOVED = "removed"
STATUS_CHANGED = "changed"
STATUS_NESTED = "nested"
STATUS_UNCHANGED = "unchanged"


def format_stylish(diff: Dict[str, Any], depth: int = 1) -> str:
    """
    Formats the diff in a stylish format.

    Parameters:
        diff (dict): The diff representation.
        depth (int): The current depth for indentation.

    Returns:
        str: The formatted stylish diff.
    """
    indent = " " * (FORMAT_INDENT_SIZE * depth - FORMAT_INDENT_OFFSET)
    lines = []

    for key, value in diff.items():
        status = value["status"]
        if status == STATUS_ADDED:
            lines.append(f"{indent}+ {key}: {
                format_value(value['value'], depth + 1)}")
        elif status == STATUS_REMOVED:
            lines.append(f"{indent}- {key}: {
                format_value(value['value'], depth + 1)}")
        elif status == STATUS_CHANGED:
            lines.append(f"{indent}- {key}: {
                format_value(value['old_value'], depth + 1)}")
            lines.append(f"{indent}+ {key}: {
                format_value(value['new_value'], depth + 1)}")
        elif status == STATUS_NESTED:
            lines.append(f"{indent}  {key}: {
                format_stylish(value['children'], depth + 1)}")
        else:
            lines.append(f"{indent}  {key}: {
                format_value(value['value'], depth + 1)}")

    closing_indent = " " * (FORMAT_INDENT_SIZE * (depth - 1))
    return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"


def format_value(value: Any, depth: int) -> str:
    """
    Formats a value for the stylish output.

    Parameters:
        value: The value to format.
        depth (int): The current depth for indentation.

    Returns:
        str: The formatted value.
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
    if "status" in value:
        return format_stylish(value, depth)

    indent = " " * (FORMAT_INDENT_SIZE * depth)
    lines = [f"{indent}{k}: {
        format_value(v, depth + 1)}" for k, v in value.items()]
    closing_indent = " " * (FORMAT_INDENT_SIZE * (depth - 1))
    return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"
