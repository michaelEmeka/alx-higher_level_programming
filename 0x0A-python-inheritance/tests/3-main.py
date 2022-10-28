is_class_kind = __import__('3-is_kind_of_class').is_kind_of_class

class Shape:
    """
    Defines a shape.
    """
    def __init__(self, name):
        """
        Instantiates a given shape.
        Args:
            name: type of shape.
        """
        self.name = name
    def print_name(self):
        """Prints the kind of shape."""
        print(self.name);

class Rect(Shape):
    """
    Defines a rectangle.
    """
    def __init__(self, name):
        """
        Instantiates a rectangle.
        """
        Shape.__init__(self, name)

rect = Rect("Rectangle")
rect.print_name()
if is_class_kind(rect, Rect):
    print("{} is an instance of {}.".format(rect, Rect))
if is_class_kind(rect, Shape):
    print("{} is an instance of {}, a subclass of {}.".format(rect, Rect, Shape))
