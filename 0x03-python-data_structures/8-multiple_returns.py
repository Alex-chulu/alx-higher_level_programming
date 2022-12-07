#!/usr/bin/python3
def multiple_returns(sentence):
    a_tuple = ()
    if len(sentence) == 0:
        a_tuple = 0, "None"
    else:
        a_tuple = len(sentence), sentence[0]
    return a_tuple
