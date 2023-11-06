#!/usr/bin/python3
"""Defines the object attrib for lookup function."""


def lookup(obj):
    """Ret the list of an object's available attributes."""
    return (dir(obj))
