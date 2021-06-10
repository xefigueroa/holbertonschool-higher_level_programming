#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """verify object is an instance(or inherited) from specified class.

    Args:
        obj: object to verify.
        a_class (type): specified class to compare with.
    Returns:
        True if obj is instance(or inherited) of a_class or False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
