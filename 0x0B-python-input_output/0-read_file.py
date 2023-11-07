#!/usr/bin/python3
"""Defines the text for file-reading function."""


def read_file(filename=""):
    """Print the text of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
