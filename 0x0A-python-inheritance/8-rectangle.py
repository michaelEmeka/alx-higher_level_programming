#!/usr/bin/python3
"""Defines a Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from 7-base_geometry.
    """
    def __init__(self, width, height):
        """
        Instantiates Rectangle instance.
        Args:
            width: width private instance attribute.
            height: height private instance attribute.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
