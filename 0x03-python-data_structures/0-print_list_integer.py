#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """To print list of integers"""
    length = len(my_list)
    for i in range(length):
        print("{:d}".format(my_list[i]))
