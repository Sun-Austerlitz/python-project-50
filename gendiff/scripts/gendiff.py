import sys

from gendiff import generate_diff
from gendiff.cli import parse_args


def main() -> None:
    """
    Main entry point for the gendiff script.
    Parses command-line arguments and generates the diff.
    """
    try:
        args = parse_args()
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
