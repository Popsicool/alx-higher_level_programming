#!/usr/bin/env python3
def no_c(my_string):
    new = ''
    for i in my_string:
        if (i != "c") and (i != "C"):
            new = new + i
    return (new)
