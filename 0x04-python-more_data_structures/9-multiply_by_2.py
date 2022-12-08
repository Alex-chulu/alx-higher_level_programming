#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    keys_list = list(new_dic.keys())

    for x in keys_list:
        new_dic[x] *= 2
    return (new_dic)
