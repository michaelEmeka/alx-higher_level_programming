#!/usr/bin/python3
def best_score(a_dictionary):
    a_dict = a_dictionary

    if a_dict is None or a_dict == {}:
        return None

    keyz = list(a_dict.keys())
    maxK = keyz[0]

    for key in keyz:
        if a_dict.get(key) > a_dict.get(maxK):
            maxK = key

    return maxK
