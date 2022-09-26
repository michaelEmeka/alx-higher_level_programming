#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    bool_list = my_list.copy()
    for i in range(length):
        bool_list[i] = my_list[i] % 2 == 0
    return bool_list
