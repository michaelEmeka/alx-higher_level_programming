#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dict = a_dictionary
    for key in a_dict:
        if a_dict.get(key) == value:
            a_dict.pop(key)
