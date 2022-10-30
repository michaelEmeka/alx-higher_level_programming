#!/usr/bin/python3
"""
Returns the dictionary description of simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of a simple data structure.
    Args:
        obj: a class instance.
    """
    return obj.__dict__
