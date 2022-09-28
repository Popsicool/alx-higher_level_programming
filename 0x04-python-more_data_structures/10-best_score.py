#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    a = None
    b = 0
    keys = a_dictionary.keys()
    for i in keys:
        if a_dictionary[i] > b:
            b = a_dictionary[i]
            a = i

    return a
