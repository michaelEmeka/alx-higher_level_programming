#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictn = a_dictionary.copy()

    for i in dictn:
        val = dictn.get(i) * 2
        dictn.update({i: val})
 
   return dictn
