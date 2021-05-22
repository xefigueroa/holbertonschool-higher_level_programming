#!/usr/bin/python3
"""Defines add int function."""


def add_integer(a, b=98):
    """Returns addition of a and b.

    Floats are changed to ints before addition.

    Raises:
        TypeError: If a or b is not int or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
