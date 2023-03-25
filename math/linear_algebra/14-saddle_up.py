#!/usr/bin/env python3
"""
performs matrix multiplication of two numpy ndarrays.
"""
import numpy as np
"""
Returns the matrix product of two arrays.
"""


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication of two numpy ndarrays.

    Args:
        mat1 (numpy.ndarray): A numpy ndarray representing the first matrix.
        mat2 (numpy.ndarray): A numpy ndarray representing the second matrix.

    Returns:
        A new numpy.ndarray representing the product of the two input matrices.

    Raises:
        ValueError: If the matrices cannot be multiplied.
    """
    # Check if matrices can be multiplied using the dot product shape rule
    assert mat1.shape[1] == mat2.shape[0], "Matrices cannot be multiplied"

    # Compute the product using np.dot and return the result
    return np.dot(mat1, mat2)
