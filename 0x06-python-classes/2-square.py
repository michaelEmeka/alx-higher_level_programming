#!/usr/bin/python3

"""
    A square Class.
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
        try:
            val = size / 1
        except TypeError:
            raise TypeError("size must be an integer")
        if size >= 0:
            val = size
        else:
            raise("size must be >= 0")

        self.__size = val
