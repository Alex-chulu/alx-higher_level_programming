#!/usr/bin/python3

if __name__ ==  "__main__":
    import sys

    num_count = len(sys.argv) - 1
    if num_count == 0:
        print("0 arguments.")
    elif num_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for x in range(num_count):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
