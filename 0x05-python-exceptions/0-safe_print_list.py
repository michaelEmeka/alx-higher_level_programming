#!/usr/bin/python3
"""Prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    if x == 0 or my_list == []:
        print()
        return 0
    for n in range(x):
        try:
            print(my_list[n], end="")
            p = n + 1
        except:
            break
    print()
    return p
