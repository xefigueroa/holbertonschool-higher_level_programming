#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0,0)):
        """Initialize a new Square.

        Args:
            size (int): size of a side of the square.
            position (int, int): position of a square.
        """
        self.size = size
        self.position = position

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
        for l in range(self.__position[1]):
            print()

        for i in range(self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print()

        if self.__size == 0:
            print("")
            return

    @property
    def position(self):
        """Getter of the __position of a square.

        Returns:
            Position of a square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of the __position of a square.

        Args:
            value (tuple): Position of a square.
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
