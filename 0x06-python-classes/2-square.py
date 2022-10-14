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
            if size >= 0:
                self.__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
