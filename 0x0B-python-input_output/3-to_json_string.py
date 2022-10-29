#!/usr/bin/python3
import json
"""Defines a json string function."""


def to_json_string(my_obj):
    """
    This function takes an object(string) and returns
    the JSON representation.

    Args:
        my_obj: an object(string).

    Returns: a JSON representation of my_obj.
    """
    return (json.dumps(my_obj))
