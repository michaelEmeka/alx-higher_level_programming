#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    maxN = my_list[0]
    if length == 1:
        return maxN
    for i in range(1, length):
        if maxN < my_list[i]:
            maxN = my_list[i]
    return maxN
