#!/usr/bin/env python3
"""
Perform element-wise addition, subtraction, multiplication,
and division on mat1 and mat2.
"""
import numpy as np


def np_elementwise(mat1, mat2):
    """
    Args:
    mat1: numpy.ndarray
    mat2: numpy.ndarray

    Returns:
    A tuple containing the element-wise sum, difference, product,
and quotient of mat1 and mat2, respectively.
    """
    sum_mat = np.add(mat1, mat2)
    diff_mat = np.subtract(mat1, mat2)
    prod_mat = np.multiply(mat1, mat2)
    quotient_mat = np.divide(mat1, mat2)

    return (sum_mat, diff_mat, prod_mat, quotient_mat)
