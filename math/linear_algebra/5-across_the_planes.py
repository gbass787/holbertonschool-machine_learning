#!/usr/bin/env python3

"""
adds two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
    """
    Parameters:
    - mat1 (list of lists of int/float): The first matrix.
    - mat2 (list of lists of int/float): The second matrix.

    Returns:
    - A new matrix containing the element-wise sum of mat1 and mat2,
or None if mat1 and mat2 are not the same shape.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    else:
        result = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[0])):
                row.append(mat1[i][j] + mat2[i][j])
            result.append(row)
        return result
