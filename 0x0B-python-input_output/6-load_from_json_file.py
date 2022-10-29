#!/usr/bin/python3
"""Creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Loads a json_file and creates an object from it."""
    with open(filename,"w+" encoding="utf-8") as f:
        read_data = f.read()
        x = json.loads(read_data)
        return (x)
