#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("{} argument".format(1))
    else:
        print("{} arguments".format(len(sys.argv) - 1))
    for i in sys.argv:
        if (sys.argv).index(i) == 0:
            pass
        else:
            print("{}: {}".format((sys.argv).index(i), i))
