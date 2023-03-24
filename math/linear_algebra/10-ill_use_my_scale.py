#!/usr/bin/env python3
"""
Return the shape of a numpy.ndarray.
"""


def np_shape(matrix):
    """
    Args:
        matrix (numpy.ndarray): An array whose shape is to be calculated.

    Returns:
        A tuple of integers representing the shape of the input matrix.

    Raises:
        None
    """
    # Use the shape attribute of the input matrix to get its shape
    return tuple(matrix.shape)
