from gendiff.read_json import read_json

"""
Constants for formatting the diff output.
"""

# if a key is present in the second file but not in the first
ADDED = "  + {key}: {value}"

# if a key is present in both files but with different values
REMOVED = "  - {key}: {value}"

# if a key is present in both files with the same value
UNCHANGED = "    {key}: {value}"

# the template for the diff output
DIFF_TEMPLATE = "{{\n{diff}\n}}"


def generate_diff(file_path1: str, file_path2: str) -> str:
    """
    Generates a diff between two JSON files.

    Parameters:
        file_path1 (str): The path to the first JSON file.
        file_path2 (str): The path to the second JSON file.

    Returns:
        str: The formatted diff between the two JSON files.
    """

    # read the JSON files
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)

    # get all keys from both files
    all_keys = sorted(set(data1.keys()).union(data2.keys()))

    # list to store the diff
    diff = []

    # compare the values for each key and add the diff to the list
    for key in all_keys:
        if key not in data2:
            diff.append(REMOVED.format(key=key, value=data1[key]))
        elif key not in data1:
            diff.append(ADDED.format(key=key, value=data2[key]))
        elif data1[key] != data2[key]:
            diff.append(REMOVED.format(key=key, value=data1[key]))
            diff.append(ADDED.format(key=key, value=data2[key]))
        else:
            diff.append(UNCHANGED.format(key=key, value=data1[key]))

    return DIFF_TEMPLATE.format(diff="\n".join(diff))
