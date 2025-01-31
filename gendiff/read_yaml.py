from typing import Any, Dict

import yaml


def read_yaml(filepath: str) -> Dict[str, Any]:
    """
    Reads a YAML file and returns its content as a dictionary.

    Parameters:
        filepath (str): The path to the YAML file to be read.

    Returns:
        Dict[str, Any]: The content of the YAML file as a dictionary.

    Raises:
        FileNotFoundError: If the file is not found at the specified path.
        ValueError: If the file contains invalid YAML.
    """
    try:
        with open(filepath, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except yaml.YAMLError:
        raise ValueError(f"Invalid YAML format in file: {filepath}")
