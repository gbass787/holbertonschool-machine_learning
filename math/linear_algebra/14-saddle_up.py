#!/usr/bin/env python3
import numpy as np
"""
performs matrix multiplication of two numpy ndarrays.
"""


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication between two numpy ndarrays

    Args:
    - mat1: numpy ndarray of shape (m, n)
    - mat2: numpy ndarray of shape (n, p)

    Returns:
    - numpy ndarray of shape (m, p) containing the
result of matrix multiplication
    """
    return np.sum(mat1[..., np.newaxis] * mat2.T, axis=-2)
