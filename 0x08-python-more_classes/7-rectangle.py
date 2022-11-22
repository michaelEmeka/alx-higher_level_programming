#!/usr/bin/python3

"""A rectangle class."""


class Rectangle:
    """
    Defines a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiates a rectangle imstance.
        Args:
            width: rectangle width.
            height: rectangle height.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        Rectangle.number_of_instances += 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        w = self.__width
        h = self.__height
        if w == 0 or h == 0:
            return 0
        return ((2 * w) + (2 * h))

    def __str__(self):
        """Prints the rectangle."""
        w = self.__width
        h = self.__height
        output = []
        if w == 0 or h == 0:
            return ""
        for i in range(h):
            for j in range(w):
                output.append(str(self.print_symbol))
            if i != h - 1:
                output.append("\n")
        return ("".join(output))

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        string = "Rectangle(" + str(self.__width)
        string += ", " + str(self.__height) + ")"
        return (string)

    def __del__(self):
        """Defines an action for an instance deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
