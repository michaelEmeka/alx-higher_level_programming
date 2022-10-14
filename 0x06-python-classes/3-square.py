#!/usr/bin/python3

"""Defines a square"""


class Square:
    """
    A Square class that defines a square.
    """
    def __init__(self, size=0):
        """
        Instantiates a Square instamce.
        Args:
            size: A new square's size.
        """
        try:
            val = size / 1
        except TypeError:
            raise TypeError("size must be an integer")

        if size >= 0:
            val = size
        else:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """
        Returns: the current square's area
        """
        return self.__size ** 2
