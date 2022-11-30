#!/usr/bin/python3
for number in range(0, 100):
    if number < 100:
        print("{}".format(number))
    else:
        print("00".format(number), end=", ")
