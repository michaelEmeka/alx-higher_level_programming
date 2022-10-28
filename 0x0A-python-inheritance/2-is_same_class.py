#!/usr/bin/python3

"""Defines a function that checks for an object's attribute."""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class.
    Args:
        obj: object.
        a_class: class.
    """
    if type(obj) == a_class:
        return (True)
    return (False)
