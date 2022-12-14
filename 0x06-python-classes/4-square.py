#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """A Square class."""

    def __init__(self, size=0):
        """
        Instantiates a square class.
        Args:
            size: A square's size.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve square's size private instance attribute.
        Returns: size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets a square's size private attribute.
        Args:
            value: square's size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns: Area of square.
        """
        return self.__size ** 2
