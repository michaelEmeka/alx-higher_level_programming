#!/usr/bin/python3
def uniq_add(my_list=[]):
    calc = 0
    passed = []
    for n in my_list:
        if n not in passed:
            calc += n
        passed.append(n)
    return calc
