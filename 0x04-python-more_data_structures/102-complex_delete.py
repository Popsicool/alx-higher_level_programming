#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.keys():
        for i in a_dictionary:
            if i == value:
                del a_dictionary[i]
    return a_dictionary
