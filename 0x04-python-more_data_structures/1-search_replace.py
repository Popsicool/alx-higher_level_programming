#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = my_list.copy()
    i = 0
    while i < len(list2):
        if list2[i] == search:
            list2[i] = replace
        i += 1
    return list2
