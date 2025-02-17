import json
from pathlib import Path
from typing import Any, Dict

import yaml


def read_file(filepath: str) -> Dict[str, Any]:
    """
    Reads the content of a file and parses it based on its extension.

    Parameters:
        filepath (str): The path to the file.

    Returns:
        dict: The parsed content of the file.
    """
    try:
        content = Path(filepath).read_text()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    extension = Path(filepath).suffix.lower()

    if extension in [".yml", ".yaml"]:
        return yaml.safe_load(content)
    elif extension == ".json":
        return json.loads(content)
    else:
        raise ValueError(f"Unsupported file format: {extension}")


def build_diff(data1: Dict[str, Any], data2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Builds a diff between two dictionaries.

    Parameters:
        data1 (dict): The first dictionary.
        data2 (dict): The second dictionary.

    Returns:
        dict: The diff representation.
    """
    keys = sorted(set(data1) | set(data2))
    diff = {}

    for key in keys:
        if key not in data1:
            diff[key] = {"status": "added", "value": data2[key]}
        elif key not in data2:
            diff[key] = {"status": "removed", "value": data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                "status": "nested",
                "children": build_diff(data1[key], data2[key]),
            }
        elif data1[key] != data2[key]:
            diff[key] = {
                "status": "changed",
                "old_value": data1[key],
                "new_value": data2[key],
            }
        else:
            diff[key] = {"status": "unchanged", "value": data1[key]}

    return diff
