#!/usr/bin/python3
"""Defines class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inherits from class rectangle"""

    def __init__(self, size):
        """initializes rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates area of square"""
        return self.__size ** 2

    def __str__(self):
        """prints string of [Square] width/height"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
