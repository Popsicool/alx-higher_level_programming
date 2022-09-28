#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list2 = []
    for i in set_1:
        if i not in set_2:
            list2.append(i)
    for i in set_2:
        if i not in set_1:
            list2.append(i)
    return list2
