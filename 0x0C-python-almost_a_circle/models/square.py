#!/usr/bin/python3
"""Defines class square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class square inherits from rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes new square.

        Args:
            size (int): Size of square.
            x (int): x coordinate of square.
            y (int): y coordinate of square.
            id (int): id of square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of size of square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size of square."""
        self.width = value
        self.height = value

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        ret = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return ret.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dictionary representation of square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
