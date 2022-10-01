#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0.00
    p = 1
    addition = 0
    divisor = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            p *= my_list[i][j]
        divisor += my_list[i][j]
        addition += p
        p = 1
    return addition / divisor
