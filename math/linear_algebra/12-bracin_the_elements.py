#!/usr/bin/env python3
"""
Perform element-wise addition, subtraction, multiplication,
and division on mat1 and mat2.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication,
and division on two numpy.ndarrays.

    Args:
        mat1 (numpy.ndarray): An array to be operated on.
        mat2 (numpy.ndarray): Another array to be operated on.

    Returns:
        A tuple containing the element-wise sum, difference, product,
and quotient, respectively.

    Raises:
        None
    """
    # numpy functions for element-wise add, sub, multi, and div
    sum_mat = np.add(mat1, mat2)
    diff_mat = np.subtract(mat1, mat2)
    prod_mat = np.multiply(mat1, mat2)
    quotient_mat = np.divide(mat1, mat2)
    return sum_mat, diff_mat, prod_mat, quotient_mat
