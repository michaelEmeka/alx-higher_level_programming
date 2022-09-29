#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    idx = new_list.index(search)
    new_list[idx] = replace
    return new_list
