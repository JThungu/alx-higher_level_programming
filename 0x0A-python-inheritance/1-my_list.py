#!/usr/bin/python3
"""This defines an inherited list class MyList."""


class MyList(list):
    """It implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """To print a list in sorted ascending order."""
        print(sorted(self))
