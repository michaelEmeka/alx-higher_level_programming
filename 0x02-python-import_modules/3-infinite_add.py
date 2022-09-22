#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    calc = 0
    for i in range(1, argc):
        calc += int(argv[i])
    print(calc)
