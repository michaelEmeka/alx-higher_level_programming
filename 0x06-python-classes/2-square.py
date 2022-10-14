#!/usr/bin/python3
"""
    A square Class.
"""

class Square:
    """
    Defines a square.
    """
    def __init__(self, size):
        """
        Initializes a square instance.
        Args:
            size: square private size instamce attribute.
            self: class instance
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        try:
            num = size / 1
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = num
