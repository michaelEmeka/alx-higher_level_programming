#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length = len(my_list)
    for i in range(length):
        print("{:d}\n".format(int(my_list[i])), end="")
