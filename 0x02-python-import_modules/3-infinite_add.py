#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    for i in sys.argv:
        if (sys.argv).index(i) == 0:
            pass
        else:
            sum += int(i)
    print("{}".format(sum))
