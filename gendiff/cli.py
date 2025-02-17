import argparse
from argparse import Namespace


def parse_args() -> Namespace:
    """
    Parses command-line arguments for the gendiff script.

    Returns:
        Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="Path to the first file")
    parser.add_argument("second_file", help="Path to the second file")
    parser.add_argument(
        "-f",
        "--format",
        help="Set format of output",
        default="stylish",
        choices=["stylish"],
    )
    return parser.parse_args()
