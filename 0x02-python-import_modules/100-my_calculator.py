#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv, exit

    argc = len(argv)
    if argc - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])

    if sign == "+":
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif sign == "-":
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif sign == "*":
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif sign == "/":
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
