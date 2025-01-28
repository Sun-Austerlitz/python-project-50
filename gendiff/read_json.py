from typing import Any, Dict
import json


def read_json(filepath: str) -> Dict[str, Any]:
    """
    Reads a JSON file and returns its content as a dictionary.

    Parameters:
        filepath (str): The path to the JSON file to be read.

    Returns:
        Dict[str, Any]: The content of the JSON file as a dictionary.

    Raises:
        FileNotFoundError: If the file is not found at the specified path.
        ValueError: If the file contains invalid JSON.
    """
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {filepath}")
