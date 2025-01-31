from gendiff.constants import ADDED, DIFF_TEMPLATE, REMOVED, UNCHANGED


def compare_data_yaml(data1, data2):
    """
    Compares two YAML files and returns the diff.

    Parameters:
        data1 (dict): The first YAML file;
        data2 (dict): The second YAML file.

    Returns:
        str: The formatted diff between the two YAML files
    """

    # get all keys from both files
    all_keys = sorted(set(data1.keys()).union(data2.keys()))

    # list to store the diff
    diff = []

    # compare the values for each key and add the diff to the list
    for key in all_keys:
        if key not in data1:
            diff.append(ADDED.format(key=key, value=data2[key]))
        elif key not in data2:
            diff.append(REMOVED.format(key=key, value=data1[key]))
        elif data1[key] != data2[key]:
            diff.append(REMOVED.format(key=key, value=data1[key]))
            diff.append(ADDED.format(key=key, value=data2[key]))
        else:
            diff.append(UNCHANGED.format(key=key, value=data1[key]))

    return DIFF_TEMPLATE.format(diff="\n".join(diff))
