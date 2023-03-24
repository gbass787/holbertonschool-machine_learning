#!/usr/bin/env python3
"""
Transpose a numpy.ndarray.
"""


def np_transpose(matrix):
    """
    Transposes a numpy.ndarray.

    Args:
        matrix (numpy.ndarray): An array to be transposed.

    Returns:
        A new numpy.ndarray representing the transposed matrix.

    Raises:
        None
    """
    # Use the transpose method of the input matrix to get its transpose
    return matrix.transpose()
