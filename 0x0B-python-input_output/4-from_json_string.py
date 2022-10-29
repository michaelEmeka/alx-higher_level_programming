#!/usr/bin/python3
"""A python json string converter."""
import json


def from_json_string(my_str):
    """
    Converts json string to python object.
    Args:
        my_str: json string.
    Return: python object(string).
    """
    return (json.loads(my_str))
