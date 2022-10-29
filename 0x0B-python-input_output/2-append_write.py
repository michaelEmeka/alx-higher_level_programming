#!/usr/bin/python3
"""Defines a file open for appending strings."""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file.

    Args:
        filename: file name.
        text: string to be appended to the file.
    Returns: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        n = f.write(text)
    return (n)
