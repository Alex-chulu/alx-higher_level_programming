#!/usr/bin/python3
x = 0
for c in range(ord('Z'), ord('a') - 1, -1):
    print("{}".format(chr(c - x)), end="")
    x = 32 if x == 0 else 0
