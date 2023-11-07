#!/usr/bin/python3
"""Defines a file-writing text function."""


def write_file(filename="", text=""):
    """Write the string to the UTF8 text file.

    Args:
        filename (str): The file name to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
