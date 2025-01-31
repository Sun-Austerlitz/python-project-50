from gendiff.compare_data_json import compare_data_json
from gendiff.read_json import read_json


def generate_diff_json(file_path1, file_path2):
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)
    return compare_data_json(data1, data2)
