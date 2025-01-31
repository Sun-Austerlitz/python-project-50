from gendiff.compare_data_yaml import compare_data_yaml
from gendiff.read_yaml import read_yaml


def generate_diff_yaml(file_path1, file_path2):
    """
    Reads two YAML files and passes them to the compare_data_yaml function
    to generate a diff.

    Parameters:
        file_path1 (str): The path to the first YAML file;
        file_path2 (str): The path to the second YAML file.

    Returns:
        str: The formatted diff between the two YAML files
        from the compare_data_yaml function
    """

    data1 = read_yaml(file_path1)
    data2 = read_yaml(file_path2)
    return compare_data_yaml(data1, data2)
