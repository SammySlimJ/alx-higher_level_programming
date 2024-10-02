#!/usr/bin/python3
"""
This module defines a class Square.

The Square class represents a geometric square and encapsulates the
size attribute, ensuring it is private to control access and modification.
"""


class Square:
    """
    Square class that defines a square by a private instance attribute.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
