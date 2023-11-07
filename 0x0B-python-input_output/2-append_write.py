#!/usr/bin/python3
"""Define the file-appending function."""


def append_write(filename="", text=""):
    """Append the string to the end of a UTF8 text file.

    Args:
        filename (str): The file name to append to.
        text (str): The string to append to the file.
    Returns:
        The number characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
