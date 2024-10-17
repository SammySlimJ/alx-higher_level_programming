#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int/float): The divisor.

    Returns:
        list of lists: A new matrix with the results.

    Raises:
        TypeError: If matrix is not a matrix of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
