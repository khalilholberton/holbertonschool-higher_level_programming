#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    c = number % 10
str = "and is less than 6 and not 0"
if number < 0:
    c = number % (10 * (-1))
if c == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, c))
elif c > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, c))
elif c < 6 and c != 0:
    print("Last digit of {:d} is {:d} {:s}".format(number, c, str))
