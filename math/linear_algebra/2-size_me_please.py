#!/usr/bin/env python3

"""
This module provides a function to calculate the shape of a matrix.
"""

def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.

    Args:
        matrix (list): A nested list representing a matrix.

    Returns:
        list: A list containing the dimensions of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
