#!/usr/bin/python3
"""
This module defines a class Square.

The Square class represents a geometric square and encapsulates the
size attribute, ensuring it is private and validated during instantiation.
"""


class Square:
    """
    Square class that defines a square by a private instance attribute.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
