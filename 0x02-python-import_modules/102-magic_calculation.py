#!/usr/bin/python3
def magic_calculation(a, b):
    """
    Performs a calculation likewise a given python bytecode.
    """
    add = __import__("magic_calculation_102").add
    sub = __import__("magic_calculation_102").sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
    return None
