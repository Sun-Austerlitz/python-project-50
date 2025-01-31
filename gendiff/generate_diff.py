from gendiff.generate_diff_json import generate_diff_json
from gendiff.generate_diff_yaml import generate_diff_yaml


def generate_diff(file_path1: str, file_path2: str) -> str:
    """
    Generates a diff between two JSON files.

    Parameters:
        file_path1 (str): The path to the first JSON file;
        file_path2 (str): The path to the second JSON file;
        format (str): The format of files.

    Returns:
        str: The formatted diff between the two JSON files
    """

    if file_path1.endswith('.json') and file_path2.endswith('.json'):
        return generate_diff_json(file_path1, file_path2)
    elif (file_path1.endswith(('.yaml', '.yml')) and
          file_path2.endswith(('.yaml', '.yml'))):
        return generate_diff_yaml(file_path1, file_path2)
    else:
        raise ValueError("Unsupported file format or mismatched file formats")
