#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    if idx >= length:
        return None
    for i in range(length):
        if i == idx:
            return my_list[i]
