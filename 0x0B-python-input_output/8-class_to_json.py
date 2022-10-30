#!/usr/bin/python3
"""Defines a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object."""


def class_to_json(obj):
    """
    Returns the dictionary description of a simple data structure.
    Args:
        obj: a class instance.
    """
    return obj.__dict__
