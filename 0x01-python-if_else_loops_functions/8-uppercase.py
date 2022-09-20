#!/usr/bin/python3
def uppercase(word):
    for i in word:
        if (ord(i) in range(97, 123)):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("\n")
