#!/usr/bin/python3

"""A rectangle class."""


class Rectangle:
    """
    Defines a rectangle.
    """
    @property
    def width(self):
        """
        Returns width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width of a rectangle.
        Args:
            value: proposed width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns height of a rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height of a rectangle.
        Args:
            value: proposed height.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """
        Instantiates a rectangle imstance.
        Args:
            width: rectangle width.
            height: rectangle height.
        """
        self.__width = width
        self.__height = height
