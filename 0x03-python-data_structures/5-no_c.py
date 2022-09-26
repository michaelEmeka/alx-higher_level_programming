#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    my_string = list(my_string)
    delim = "cC"
    for i in range(length):
        if length[i] in delim:
            my_string.remove(my_string[i])
    my_string = "".join(my_string)
    return my_string
