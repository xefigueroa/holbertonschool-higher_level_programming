#!/usr/bin/python3
"""Defines inherited list class."""


class MyList(list):
    """Class that inherits from list."""

    def print_sorted(self):
        """Prints list but sorted ascending order."""
        print(sorted(self))
