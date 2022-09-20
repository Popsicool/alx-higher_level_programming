#!/usr/bin/python3
def uppercase(word):
    count = 0
    for i in word:
        if (ord(i) in range(97, 123)):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
        count += 1
        if (count == len(word)):
            print()
