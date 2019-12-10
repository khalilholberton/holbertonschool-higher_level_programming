#!/usr/bin/python3
for c in range(0, 99):
    if c <= 9:
        print(0, end="")
    print("{}".format(c), end=", " if c < 98 else ', {}\n'.format(99))
