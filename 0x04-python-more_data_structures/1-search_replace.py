#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda y: replace if y == search else y, my_list))
    return (new_list)
