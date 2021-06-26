#!/usr/bin/python3
"""Define class Base"""


class Base:
    """Defines class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new Base

        Args:
            id (int): id of Base
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
