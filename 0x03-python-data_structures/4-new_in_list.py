#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp = my_list.cp()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.cp()
    else:
        cp[idx] = element
        return cp
