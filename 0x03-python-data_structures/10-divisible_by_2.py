#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    two_list = []
    for i in my_list:
        if i % 2 == 0:
            two_list.append(True)
        else:
            two_list.append(False)
    return two_list
