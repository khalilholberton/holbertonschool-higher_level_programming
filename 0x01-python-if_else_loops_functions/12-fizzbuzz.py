#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 15 == 0:
            fb = "FizzBuzz"
        elif number % 3 == 0:
            fb = "Fizz"
        elif number % 5 == 0:
            fb = "Buzz"
        else:
             = number
        print("{} ".format(fb), end="")
