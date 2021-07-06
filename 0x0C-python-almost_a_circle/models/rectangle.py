#!/usr/bin/python3
"""Defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines class Rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inits a Rectangle

        Args:
            width (int): width of rect
            height (int): height of rect
            x (int): Coord x
            y (int): Coord y
            id (int): id of rect

        Raises:
            TypeError: If the input is not an integer
            ValueError: If width or height is under or equals 0
            ValueError:If x or y is under 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width of Rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height of Rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter x coord of Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x coord of Rectangle."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter y coord of Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y coord of Rectangle."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of Rectangle."""
        return self.width * self.height

    def display(self):
        """Prints rectangle representation with #"""
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                    print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        ret = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return ret.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
