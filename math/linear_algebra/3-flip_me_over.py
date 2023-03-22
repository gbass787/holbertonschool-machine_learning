#!/usr/bin/env python3

def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of lists): 2D matrix

    Returns:
        list of lists: Transposed matrix
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transposed = []
    for i in range(num_cols):
        transposed.append([matrix[j][i] for j in range(num_rows)])
    return transposed
