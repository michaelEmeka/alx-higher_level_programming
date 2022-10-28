#!/usr/bin/python3
"""Defines a function that checks for kind of class."""

def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or another class
    that inherits from a_class.

    Args:
        obj: object.
        a_class: class.

    Returns: True if obj is a_class instance or a_class
             subclass instance.
             Else: returns False.

    """
    if type(obj) == a_class:
        return (True)
    if issubclass(type(obj), a_class):
        return (True)

    return (False)
