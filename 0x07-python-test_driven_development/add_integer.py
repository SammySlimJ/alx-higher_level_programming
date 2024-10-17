#!/usr/bin/python3
"""
This module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Parameters:
    a (int or float): The first number to add.
    b (int or float, optional): The second number to add. Defaults to 98.

    Raises:
    TypeError: If a or b are not integers or floats.

    Returns:
    int: The sum of a and b, casted to an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
