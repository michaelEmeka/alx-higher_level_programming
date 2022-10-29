#!/usr/bin/python3
"""Takes CL arguments and convert them to object put in a file."""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        obj = load_from_json_file("add_item.json")
    except FileNotFoundError:
        obj = []
    obj.extend(argv[1:])
    save_to_json_file(obj, "add_item.json")
