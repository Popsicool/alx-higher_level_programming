#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    while (count < x and count < len(my_list)):
        try:
            print(my_list[count], end="")
            count += 1
        except (RuntimeError, TypeError, NameError, IndexError):
            pass
    print()
    return (count)
