#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while (count < x and count < len(my_list)):
            print(my_list[count], end="")
            count += 1
        print()
        return (count)
    except (RuntimeError, TypeError, NameError, IndexError):
        pass
