#!/usr/bin/python3
"""Creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Loads a json_file and creates an object from it."""
    with open(filename, encoding="utf-8") as f:
        x = json.load(f)
        return (x)
