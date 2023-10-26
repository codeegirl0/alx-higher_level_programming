#!/usr/bin/python3
"""find max integer module
"""


def max_integer(list=[]):
    """Function to find amax int in a list
     or return None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
