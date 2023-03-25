#!/usr/bin/env python3
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
    """
    if mat1.shape[1] != mat2.shape[0]:
        raise ValueError("Matrices cannot be multiplied")

    return np.dot(mat1, mat2)
