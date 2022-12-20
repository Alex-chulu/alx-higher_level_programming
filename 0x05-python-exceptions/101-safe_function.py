#!/usr/bin/python3

from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        rmp = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
    else:
        return rmp
