#!/usr/bin/python3
"""Start a class-checking function."""


def is_same_class(obj, a_class):
    """Checking if an object exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    to return:
        If obj is exactly an instance of a_class - True.
        or False.
    """
    if type(obj) == a_class:
        return True
    return False
