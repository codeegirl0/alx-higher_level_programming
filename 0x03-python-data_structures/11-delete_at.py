#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """get out of list"""
    new_list = []
    if idx >= 0 and idx < len(my_list):
        new_list = my_list
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    return (new_list)
