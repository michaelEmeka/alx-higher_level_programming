#!/usr/bin/python3
"""Modifies a text file."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename: name of file.
        search_string: string in search for.
        new_string: string to be appended to current searchline
        where search_string is found.
    """
    with open(filename, encoding="utf-8") as f:
        data = f.readlines()

    for line in range(len(data)):
        newL = data[line]
        if search_string in newL:
            newL += new_string
        data[line] = newL

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(data)
