#!/usr/bin/python3
"""Define the JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return a Python object representation of a JSON string."""
    return json.loads(my_str)
