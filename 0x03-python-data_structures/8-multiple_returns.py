#!/usr/bin/python3
def multiple_returns(sentence):
    return_tuple = ()
    length = len(sentence)
    if length == 0:
        return_tuple = 0, "None"
    else:
        return_tuple = length, sentence[0]
    return return_tuple
