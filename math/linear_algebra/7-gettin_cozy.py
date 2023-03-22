#!/usr/bin/env python3
"""
Concatenates two matrices along a specific axis.
"""
import numpy as np


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray): The second matrix.
        axis (int, optional): The axis along which to concatenate
the matrices. Default is 0.

    Returns:
        numpy.ndarray or None: The concatenated matrix, or None
if the matrices cannot be concatenated.
    """
    try:
        return np.concatenate((mat1, mat2), axis=axis)
    except ValueError:
        return None
