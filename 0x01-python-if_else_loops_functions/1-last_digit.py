#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    num = number % 10
str = "and is less than 6 and not 0"
if number < 0:
    num = number % (10 * (-1))
if num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
elif num > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, num))
elif num < 6 and num != 0:
    print("Last digit of {} is {} and {}".format(number, num, str))
