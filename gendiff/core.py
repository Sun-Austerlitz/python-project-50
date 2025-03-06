import json
from pathlib import Path
from typing import Any, Dict

import yaml


def read_file(filepath: str) -> str:
    """
    Reads the content of a file.

    Parameters:
        filepath (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    try:
        return Path(filepath).read_text()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")


def parse_data(data: str, format: str) -> Dict[str, Any]:
    """
    Parses the data based on its format.

    Parameters:
        data (str): The data to parse.
        format (str): The format of the data (e.g., 'json', 'yaml').

    Returns:
        dict: The parsed data.
    """
    if format in ["yml", "yaml"]:
        return yaml.safe_load(data)
    elif format == "json":
        return json.loads(data)
    else:
        raise ValueError(f"Unsupported data format: {format}")


def get_file_format(filepath: str) -> str:
    """
    Gets the format of the file based on its extension.

    Parameters:
        filepath (str): The path to the file.

    Returns:
        str: The format of the file.
    """
    return Path(filepath).suffix.lower().lstrip(".")
