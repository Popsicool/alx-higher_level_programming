#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.keys():
        pos = []
        for i in a_dictionary:
            if i == value:
                pos.append(a)
        for i in pos:
            del a_dictionary[i]
    return a_dictionary
