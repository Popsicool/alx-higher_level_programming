#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
state = 0
if (number > -1):
    state = 1
else:
    state = -1
number = number * (-1)
last_num = (number % 10) * state
number = number * state

if (last_num == 0):
    print("Last digit of {} is {} and 0".format(number, last_num))
elif (last_num > 5):
    print("Last digit of {} is {} and is greater than 5 and not 0".format(number, last_num))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_num))
