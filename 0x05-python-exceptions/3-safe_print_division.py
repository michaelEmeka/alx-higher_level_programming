#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two integers and prints the result using
    try: / except: / finally, {:d}.format.

    Args:
        a - dividend
        b - divisor
    """
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {:d}".format(div))
    return div
