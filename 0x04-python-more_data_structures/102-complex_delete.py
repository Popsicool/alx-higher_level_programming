#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    pos = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            pos.append(i)
    for i in pos:
        del a_dictionary[i]
    return a_dictionary
