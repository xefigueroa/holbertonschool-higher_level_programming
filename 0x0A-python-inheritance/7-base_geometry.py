#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Measures area. (Not implemented)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name (str): name.
            value (int): value to validate.
        Raises:
            TypeError: if value is not int
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
