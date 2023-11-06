#!/usr/bin/python3
"""the module inherits from the list class"""


class MyList(list):
    """A class to inherits from list"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
