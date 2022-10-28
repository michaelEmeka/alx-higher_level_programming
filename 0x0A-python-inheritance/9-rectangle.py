#!/usr/bin/python3
"""
Defines a class Inherits from BaseGeometry (7-base_geometry)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class.
    """
    def __init__(self, width, height):
        """
        Instantiates a Rectangle object.
        Args:
            width: rectangle private instance attribute.
            height: rectangle private instance attribute.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.__des__ = "hell"
    def __str__(self):
        """
        Defines print() and str() for class instances.
        Returns:
            [Rectangle] <width>/<height>
        """
        strin = "[{}]".format(str(self.__class__.__name__))
        strin += " {}/{}".format(self.__width, self.__height)
        return (strin)

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return (self.__width * self.__height)

