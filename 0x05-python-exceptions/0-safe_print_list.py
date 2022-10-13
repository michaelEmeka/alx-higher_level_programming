#usr/bin/python3
"""Prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    for n in range(x):
        try:
            print(my_list[n], end="")
        except:
            break
    print();
    return n + 1
