#!/usr/bin/env python3
import numpy as np
"""
Returns the matrix product of two arrays.
"""


def np_matmul(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    """
    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The product of the two matrices.

    Raises:
        ValueError: If the matrices have incompatible dimensions.
    """
    return np.matmul(mat1, mat2)
