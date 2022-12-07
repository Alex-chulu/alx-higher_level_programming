#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    first_tuple = tuple_a + (0, 0)
    second_tuple = tuple_b + (0, 0)
    new_tuple = first_tuple[0] + second_tuple[0], first_tuple[1] + second_tuple[1]
    return new_tuple
