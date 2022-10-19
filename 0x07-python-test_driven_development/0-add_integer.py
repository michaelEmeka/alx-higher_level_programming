#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function adds two integers and returns their sum.

    Args:

        a: first integer/float value.
        b: second integer/float value.

    Return: the sum of a and b(a + b).
    """
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(a, float):
            a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, int) or isinstance(b, float):
        if isinstance(b, float):
            b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
