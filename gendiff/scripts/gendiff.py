import argparse

from gendiff.generate_diff import generate_diff


# entry point
def main():
    # create parser
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    # add arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # add optional arguments
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        dest="format",
    )

    # parse arguments
    args = parser.parse_args()

    # try to read files and generate diff
    try:
        result = generate_diff(args.first_file, args.second_file)
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
