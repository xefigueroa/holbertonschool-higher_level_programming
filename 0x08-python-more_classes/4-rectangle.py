#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle

        Args:
            width (int): width of a rectangle.
            height (int): height of a rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for rectangle width

        Raises:
            TypeError: If width is not int.
            ValueError: If width less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for rectangle height

        Raises:
            TypeError: If height is not int.
            ValueError: If height less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns representation of rectangle(#)"""
        if not self.width or not self.height:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """Returns string representation of rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
