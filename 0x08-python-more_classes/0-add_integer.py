#!/usr/bin/python3

#0-add_integer.py
"""This defines a function for adding integers."""

def add_integer(a, b=98):
    """Return the sum of two integers.

    Float arguments are converted to integers before the addition is performed.

    Raises:
        TypeError: If either `a` or `b` is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    return int(a) + int(b)
