#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print reversed integers"""
    if isinstance(my_list, list):
        new_list = my_list.reverse()
        my_list = new_list
        for i in my_list:
            print("{:d}".format(i))
