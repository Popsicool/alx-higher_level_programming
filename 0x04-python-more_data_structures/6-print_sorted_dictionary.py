#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_keys = sorted(a_dictionary.keys())
    for i in list_of_keys:
        print("{}: {}".format(i, a_dictionary[i]))
