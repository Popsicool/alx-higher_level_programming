#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    words = list(roman_string)
    all = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    i = 1
    sum = all[words[0]]
    while (i < len(words)):
        if (words[i - 1] == "I") and (words[i] == ("X" or "V")):
            sum -= 2
        sum += all[words[i]]
        i += 1
    return sum
