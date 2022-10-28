#!/usr/bin/python3
"""Defines a square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class.
    """
    def __init__(self, size):
        """
        Instantiates a square.
        Args:
            size: private instance attribute(square size).
        """
        self.integer_validator("size", size)
        self.__size = size
        self.__height = size
        self.__width = size
        super().__init__(size, size)
