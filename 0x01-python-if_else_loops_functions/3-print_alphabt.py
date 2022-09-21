#!/usr/bin/python3
for letter in range(97, 123):
    if char(letter) == 'q' or char(letter) == 'e':
        continue
    else:
        print("{}".format(chr(letter)), end = "")
