#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = 0
if number < 0:
    lastdigit = -(-number % 10)
else:
    lastdigit = number % 10
if lastdigit > 5:
    print(f"Last digit of {number:d} is {lastdigit:d} and is greater than 5")
elif lastdigit == 0:
    print(f"Last digit of {number:d} is {lastdigit:d} and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print(f"Last digit of {number:d} is {lastdigit:d} and is less than 6 and not 0")
