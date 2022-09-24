#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenth1 = len(tuple_a)
    lenth2 = len(tuple_b)
    if lenth1 < 2:
        try:
            a = tuple_a[0]
        except Exception:
            a = 0
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]

    if lenth2 < 2:
        try:
            c = tuple_b[0]
        except Exception:
            c = 0
        d = 0
    else:
        c = tuple_b[0]
        d = tuple_b[1]
    e = a + c
    f = b + d

    new = (e, f)
    return (new)
