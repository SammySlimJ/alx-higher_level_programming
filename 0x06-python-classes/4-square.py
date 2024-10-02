#!/usr/bin/python3
"""
This module defines a class Square.

The Square class represents a geometric square and encapsulates the
size attribute, ensuring it is private and validated during instantiation
and when accessing or modifying the size.
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
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
