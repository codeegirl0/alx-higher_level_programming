#!/usr/bin/python3
"""Start an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checking if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Return:
        If obj is an inherited instance of a_class - True.
        or - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
