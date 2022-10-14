#!/usr/bin/python3

"""Defines a square"""


class Square:
    """A Square class"""

    def __init__(self, size=0):
        """
        Instantiates a square class.
        Args:
            size: A square's size.
        """
        try:
            num = size / 1
        except TypeError
            raise TypeError("size must be an integer")

        if size >= 0:
            num = size
        else:
            raise ValueError("size must be >= 0")
        self.__size = num

    def size(self):
        """
        Retrieve square's size private instance attribute.
        Returns: size.
        """
        return self.__size

    def size(self, value):
        """
        Sets a square's size private attribute.
        Args:
            value: square's size
        """
        try:
            num = size / 1
        except TypeError
            raise TypeError("size must be an integer")

        if size >= 0:                                                       num = size
        else:
            raise ValueError("size must be >= 0")
        self.__size = num

    def area(self):
        """
        Returns: Area of square.
        """
        return self.__size ** 2

