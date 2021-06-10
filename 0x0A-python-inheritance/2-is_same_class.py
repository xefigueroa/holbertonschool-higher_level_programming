#!/usr/bin/python3
"""Defines a function that checks if object is same class"""


def is_same_class(obj, a_class):
    """Verifies if the object is exactly an instance of the specified class.

    Args:
        obj: object to verify
        a_class (type): specified class to compare with.
    Returns:
        True if instance of specified class or False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
