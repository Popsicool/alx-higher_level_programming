#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    lent = 0
    while (lent < x):
        try:
            print(my_list[count], end="")
            count += 1
            lent += 1
        except (RuntimeError, TypeError, NameError, IndexError):
            lent += 1
    print()
    return (count)
