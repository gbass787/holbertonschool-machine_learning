#!/usr/bin/env python3
"""
Perform element-wise addition, subtraction, multiplication,
and division on mat1 and mat2.
"""
import numpy as np


def np_elementwise(mat1, mat2):
    # Element-wise sum
    sum_mat = np.add(mat1, mat2)

    # Element-wise difference
    diff_mat = np.subtract(mat1, mat2)

    # Element-wise product
    prod_mat = np.multiply(mat1, mat2)

    # Element-wise quotient
    quo_mat = np.divide(mat1, mat2)

    return sum_mat, diff_mat, prod_mat, quo_mat
