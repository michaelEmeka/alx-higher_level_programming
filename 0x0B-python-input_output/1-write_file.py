#!/usr/bin/python3
"""Defines a file write function."""


def write_file(filename="", text=""):
    """
    Opens a file and writes into it using UTF-8 encoding.
    Args:
        filename: name of file.
        text: text to be added to file.
    Description: -creates the file if it doesn’t exist,
                 -overwrite the content of the file if it
                 already exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        n = f.write(text)
    return (n)
