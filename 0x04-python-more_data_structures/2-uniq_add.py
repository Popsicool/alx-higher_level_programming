#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    list2 = []
    for i in my_list:
        if i not in list2:
            add += i
            list2.append(i)
    return add
