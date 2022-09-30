#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_k = sorted(a_dictionary)

    for i in range(len(sorted_k)):
        key = sorted_k[i]
        print("{} : {}".format(key, a_dictionary.get(key)))
