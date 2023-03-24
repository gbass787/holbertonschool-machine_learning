#!/usr/bin/env python3
import numpy as np
"""
Concatenates two matrices along a specific axis.
"""


def np_cat(mat1, mat2, axis=0):
    """
    Parameters:
        mat1 (numpy.ndarray): The first matrix to concatenate.
        mat2 (numpy.ndarray): The second matrix to concatenate.
        axis (int, optional): The axis along which to concatenate the matrices.
            Default is 0.

    Returns:
        numpy.ndarray: The concatenated matrix.

    Raises:
        ValueError: If the shapes of the matrices are not compatible
for concatenation.

    """
    try:
        return np.concatenate((mat1, mat2), axis=axis)
    except ValueError as e:
        raise ValueError("Matrices are not compatible for concatenation.") from e
