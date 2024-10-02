#!/usr/bin/python3
"""
This module defines a class Square.

The Square class represents a geometric square and encapsulates the
size and position attributes, ensuring they are private and validated
during instantiation and when accessing or modifying the attributes.
"""


class Square:
    """
    Square class that defines a square by private instance attributes.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square on a grid.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not
                a tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position values
                are negative.
        """
        self.size = size  # Use the setter for size validation
        self.position = position  # Use the setter for position validation

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If the position values are negative.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character #.

        If size is 0, prints an empty line.
        Position is considered by using spaces to offset the square.
        """
        if self.__size == 0:
            print()  # Print an empty line if size is 0
            return

        # Print empty lines before the square according to the y position
        for _ in range(self.__position[1]):
            print()  # Print new lines for the vertical position

        # Print the square with leading spaces according to the x position
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
