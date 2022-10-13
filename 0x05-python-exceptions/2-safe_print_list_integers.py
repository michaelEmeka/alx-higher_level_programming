#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    This function prints a list of integers.

    Args:
        my_list: list to be printed
        x: number of elements in my_list to be printed

    Using:
        try:/except, {:d}.format
    """
    p = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p += 1
        except(TypeError, ValueError):
            continue
        except IndexError:
            break
