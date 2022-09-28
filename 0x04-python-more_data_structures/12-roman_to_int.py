#!/usr/bin/python3
def roman_to_int(roman_string):
    if (isinstance(roman_string, str) is False) or (roman_string is None):
        return 0
    words = list(roman_string)
    all = {"D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    i = 1
    sum = all[words[0]]
    while (i < len(words)):
        if (words[i - 1] == "I") and (words[i] == ("X" or "V")):
            sum -= 2
        sum += all[words[i]]
        i += 1
    return sum
