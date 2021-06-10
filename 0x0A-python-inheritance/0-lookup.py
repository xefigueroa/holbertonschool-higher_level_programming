#!/usr/bin/python3
"""returns list of available attributes and methods of an object."""


def lookup(obj):
    """looks for avail attr and methods of an obj.

    Args:
        obj (object): object to list.

    Returns:
        list: list of attr.
    """
    return dir(obj)
