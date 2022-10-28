#!/usr/bin/python3

"""Defines a sub class checking function."""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class
    that inherited (directly or indirectly) from
    a_class.

    Args:
        obj: object instance.
        a_class: class.

    Returns:
        True: if obj is an instance.
        Flase: if otherwise.
    """
    if type(obj) == a_class:
        return (False)
    if issubclass(type(obj), a_class):
        return (True)

    return (False)
