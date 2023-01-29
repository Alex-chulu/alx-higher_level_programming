#!/usr/bin/python3
""" A class MyList, inherits from list """


class MyList(list):
    """This is a public instance method and it prints the list, but sorted (ascending sort)

    Arguments:
        list: A list class
    """
    def print_sorted(self):
        print(sorted(self))

