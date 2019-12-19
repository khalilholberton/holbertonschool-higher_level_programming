#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for res in sorted(a_dictionary.keys()):
        print("{}: {}".format(res, a_dictionary[res]))
