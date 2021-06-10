#!/usr/bin/python3
"""Defines functions that verifies class inheritance."""


def inherits_from(obj, a_class):
    """Verifies obj instance of class that inherited(dir/ind) from a_class.

    Args:
        obj: object to verify.
        a_class (type): specified class to compare with.
    Returns:
        True if obj is inherited inst of a_class or False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
