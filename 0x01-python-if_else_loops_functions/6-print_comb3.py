#!/usr/bin/python3
for i in range(100):
    first_num = int(i / 10)
    last_num = i % 10
    if (first_num < last_num):
        if (i != 89):
            print("{:02d}".format(i), end=", ")
        else:
            print("{}".format(i))
