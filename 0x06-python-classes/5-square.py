#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): size of a side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter of the __size of the side of a square.

        Returns:
            Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of the __size of the side of a square.

        Args:
            value (int): the size of a size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Evaluates the area of a square.

        Returns:
            Area of a square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print square."""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
