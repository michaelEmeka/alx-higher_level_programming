#!/usr/bin/python3

"""
    Defines a square Class.
"""


class Square:
    """
    Defines a square.
    """
    def __init__(self, size=0):
        """
        Initializes a square instance.
        Args:
            size: square private size instamce attribute.
            self: class instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
