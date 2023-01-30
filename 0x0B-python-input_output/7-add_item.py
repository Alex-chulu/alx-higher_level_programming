#!/usr/bin/python3
"""script that adds all arguments to a Python list, and then save them to a file"""


import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    filename = "add_item.json"
    if os.path.isfile(filename):
        "check if the file already exist"
        load_file = load_from_json_file(filename)
        "load the file if it exist"
        load_file += sys.argv[1:]
        "adds all arguments to a Python list"
        save_to_json_file(list(load_file), filename)
        "save them to a file"
    else:
        "If the file doesn’t exist, it should be created"
        save_to_json_file(sys.argv[1:], filename)
