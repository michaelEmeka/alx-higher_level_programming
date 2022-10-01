#!/usr/bin/python3
def roman_to_int(roman_string):
    rome = {'M' : 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V': 5, 'I':1}
    rS = roman_string

    if rS is None or type(rS) is not str:
        return 0
    output = 0
    prev = 0
    for val in rS:
        curr = rome.get(val)
        if curr <= prev:
            output += curr
        else:
            output += curr - prev - prev
        prev = curr
    return output
