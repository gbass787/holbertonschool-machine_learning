#!/usr/bin/env python3
"""
Concatenates two matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Args:
        mat1 (list[list]): A 2D matrix containing ints/floats
        mat2 (list[list]): A 2D matrix containing ints/floats
        axis (int): The axis along which to concatenate the matrices.
            If axis=0, concatenate rows; if axis=1, concatenate columns.
            Default is 0.

    Returns:
        A new 2D matrix containing the concatenated matrices, or None if the
        matrices cannot be concatenated along the specified axis.

    Raises:
        None
    """
    # Ensure that mat1 and mat2 have same shape in the non-concatenated axis
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    elif axis == 1 and len(mat1) != len(mat2):
        return None

    # Concatenate the matrices along the specified axis
    if axis == 0:
        return [row for row in mat1] + [row for row in mat2]
    elif axis == 1:
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
