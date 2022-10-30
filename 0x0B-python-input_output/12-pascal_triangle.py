#!/usr/bin/python3
"""Creates a pascal triangle."""


def pascal_triangle(n):
    """
    Creates a list of lists of a pascal's triangle.
    Args:
        n: power(or number of rows)
    Returns:
        A list pf lists representing a pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

