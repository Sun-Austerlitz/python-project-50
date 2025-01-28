import argparse

from gendiff.scripts.read_json import read_json


# точка входа
def main():
    # создаем парсер аргументов
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    # добавляем аргументы
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # добавляем аргумент для формата вывода
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        dest="format",
    )

    # парсим аргументы
    parser.parse_args()

    # читаем файлы
    file1 = read_json("file1.json")
    file2 = read_json("file2.json")

    # выводим файлы как json строки
    print(f"file1: {file1}")
    print(f"file2: {file2}")


if __name__ == "__main__":
    main()
