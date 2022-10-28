#!/usr/bin/python3
"""Defines a square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class inherited from a rectangle class.
    """
    def __init__(self, size):
        """
        Instantiates a square.
        Args:
            size: square size(a private instance attribute)
        """
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size
        super().__init__(size, size)
