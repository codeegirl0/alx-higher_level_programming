#!/usr/bin/python3
"""start a class MyInt that inherits from int."""


class MyInt(int):
    """inv int operators == and !=."""

    def __eq__(self, value):
        """rewrite == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """rewrite != operator with == behavior."""
        return self.real == value
