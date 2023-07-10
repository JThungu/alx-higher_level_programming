#!/usr/bin/python3
"""This defines an object attribute lookup function."""


def lookup(obj):
    """To return a list of an object available attributes."""
    return (dir(obj))
