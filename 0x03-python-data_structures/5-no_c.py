#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Deleting c and C in a string."""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and i != 'C':
            return ("".join(my_string[i]))
