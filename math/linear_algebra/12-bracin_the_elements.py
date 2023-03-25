#!/usr/bin/env python3
"""
Perform element-wise addition, subtraction, multiplication,
and division on mat1 and mat2.
"""


def np_elementwise(mat1, mat2):
    """Perform element-wise addition, sub, multiplication, and division.

    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray): The second matrix.

    Returns:
        tuple: A tuple containing the element-wise sum, difference, product,
        and quotient, respectively.
    """
    sum_arr = mat1 + mat2
    diff_arr = mat1 - mat2
    prod_arr = mat1 * mat2
    quotient_arr = mat1 / mat2

    return (sum_arr, diff_arr, prod_arr, quotient_arr)
