#!/usr/bin/python3
"""Writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function creates a json file.
    Args:
        my_obj: python object.
        filename: json representation file name.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
