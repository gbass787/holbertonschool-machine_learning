#!/usr/bin/env python3

"""
Performs matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Parameters:
    - mat1 (list of lists of int/float): The first matrix.
    - mat2 (list of lists of int/float): The second matrix.

    Returns:
    - A new matrix containing the result of the matrix multiplication of
mat1 and mat2, or None if the matrices cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None
    else:
        result = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat2[0])):
                sum = 0
                for k in range(len(mat2)):
                    sum += mat1[i][k] * mat2[k][j]
                row.append(sum)
            result.append(row)
        return result
