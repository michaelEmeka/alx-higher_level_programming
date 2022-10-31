#!/usr/bin/python3

"""Defines a class BaseGeometry."""


class BaseGeometry:
    """
    A class.
    """
    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented");

    def integer_validator(self, name, value):
        """
        This function validates value.
        Args:
            name: integer variable name.
            value: an integer.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
