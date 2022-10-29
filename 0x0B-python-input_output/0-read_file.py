#!/iusr/bin/python3
"""Defines a file function."""


def read_file(filename=""):
    """
    Reads a text file using text using UTF-8 encoding
    and prints it to stdout.

    Args:
        filename: the file name.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
