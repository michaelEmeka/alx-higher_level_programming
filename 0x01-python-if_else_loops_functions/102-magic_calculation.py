#!/usr/bin/python3
def magic_calculation(a, b, c):
    """
    A reverse interpretation of a python bytecode.
    """
    if a < b:
        return c
    elif c < b:
        return (a + b)
    else:
        return (a * b) - c
