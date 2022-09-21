#!/usr/bin/python3
lower = True
temp = 25
while temp >= 0:
    if lower is True:
        print("{}".format(chr(97 + temp)), end="")
        lower = False
        temp = temp - 1
    else:
        print("{}".format(chr(97 + temp - 32)), end="")
        lower = True
        temp = temp - 1
