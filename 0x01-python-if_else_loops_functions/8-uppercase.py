#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(length):
        asci = ord(str[i])
        if asci > 96 and asci < 124:
            asci -= 32
        print("{}".format(chr(asci)), end="")
    print("")
