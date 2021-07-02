#!/usr/bin/python3
"""Defines class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle which inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints a string of width/height"""
        return "[Rectangle] " + \
            str(self.__width) + "/" + str(self.__height)
