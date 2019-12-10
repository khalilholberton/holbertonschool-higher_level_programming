#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
afterfive = 'is greater than 5'
zero = 'is 0'
beforesix = ' is less than 6 and not 0'
if (number % 10 > 5):
    print('Last digit of {} is {} {}'.format(number, number % 10, afterfive))
elif (number % 10 == 0):
    print('Last digit of {} is {} {}'.format(number, number % 10, zero))
elif (number < 0):
    print('Last digit of {} is -{} {}'.format(number, (number * -1) % 10, beforesix))
else:
    print('Last digit of {} is {} {}'.format(number, number % 10, beforesix))
