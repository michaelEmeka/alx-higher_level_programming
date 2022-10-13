#!/usr/bin/python3
"""Prints Integer"""


def safe_print_integer(value):
    """
    Prints an integer using {:d} and try:, except.

    Args:
        value: argument of any type.

    Return:
        True - on success(if value is of :d type).
        False - on failure.
    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
