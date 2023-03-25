#!/usr/bin/env python3
"""
not enough documentation it seems.
"""
import numpy as np
"""
Concatenates two matrices along a specific axis.
"""


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (numpy.ndarray): A numpy ndarray to be concatenated.
        mat2 (numpy.ndarray): A numpy ndarray to be concatenated.
        axis (int, optional): The axis along which the matrices
are concatenated. Default is 0.

    Returns:
        A new numpy.ndarray containing the concatenated matrices.
    """
    return np.concatenate((mat1, mat2), axis=axis)
