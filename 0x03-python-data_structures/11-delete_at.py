#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list
    for i in range(length):
        if i == idx:
            my_list.remove(my_list[idx])
            return my_list
