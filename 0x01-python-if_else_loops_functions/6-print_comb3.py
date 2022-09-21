#!/usr/bin/python3
for tens in range(0, 8):
    for units in range((tens + 1), 10):
        print("{:d}{:d}, ".format(tens, units), end="")
print("{:d}".format(89))
