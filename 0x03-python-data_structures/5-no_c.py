#!/usr/bin/python3
def no_c(my_string):
    """
    Removes 'c' or 'C' from my_string and returns a new string.
    """
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
