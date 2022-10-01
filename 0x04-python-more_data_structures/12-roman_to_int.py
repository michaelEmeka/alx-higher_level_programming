#!/usr/bin/python3
def roman_to_int(roman_string):
    rome = {'M' : 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V': 5, 'I':1}
    rS = roman_string

    if rS is None or type(rS) is not str:
        return None
	output = 0
	prev = 1001

    for val in rS:
        curr = int(rome.get(val))
        if curr <= prev:
            output += curr
        else:
            if output > curr:
                output -= curr
            else:
                output = (output - curr) * -1
                prev = curr
    return output
