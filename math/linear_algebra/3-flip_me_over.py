#!/usr/bin/env python3

def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of lists): A 2D matrix of values. Each element is a list,
                                representing a row of the matrix.

    Returns:
        list of lists: The transposed matrix. Each element is a list,
                       representing a column of the matrix.

    Raises:
        IndexError: If the input matrix is empty or has unequal row sizes.

    Examples:
        >>> matrix_transpose([[1, 2], [3, 4], [5, 6]])
        [[1, 3, 5], [2, 4, 6]]

    """
    # get the number of rows and columns in the input matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # initialize an empty matrix to store the transposed values
    transposed = []

    # iterate through each column of the input matrix
    for i in range(num_cols):
        # extract the values of the i-th column and append them to transposed
        transposed.append([matrix[j][i] for j in range(num_rows)])

    return transposed
