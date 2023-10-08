#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    newstr = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(newstr))
