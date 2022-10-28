#!/usr/bin/python3
"""Defines an object attribute adder."""


def add_attribute(obj, attrib, value):
    """
    Adds an attribute to obj, and assigns a value to it.
    Args:
        obj: object(class instance).
        attrib: new attribute to be added.
        value: obj attribute value.
    Raises:
        TypeError on failure.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attrib, value)
