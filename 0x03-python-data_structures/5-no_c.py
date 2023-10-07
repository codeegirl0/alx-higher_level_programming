#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [i for i in my_string if i != 'c' and x != 'C']
    return ("".join(copy))
