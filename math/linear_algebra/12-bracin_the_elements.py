#!/usr/bin/env python3
"""
Perform element-wise addition, subtraction, multiplication,
and division on mat1 and mat2.
"""


def np_elementwise(mat1, mat2):
    # Get the shape of the matrices
    shape = mat1.shape

    # Reshape the matrices as 1D arrays
    mat1_1d = mat1.reshape(-1)
    mat2_1d = mat2.reshape(-1)

    # Element-wise sum
    sum_mat_1d = [mat1_1d[i] + mat2_1d[i] for i in range(len(mat1_1d))]
    sum_mat = np.array(sum_mat_1d).reshape(shape)

    # Element-wise difference
    diff_mat_1d = [mat1_1d[i] - mat2_1d[i] for i in range(len(mat1_1d))]
    diff_mat = np.array(diff_mat_1d).reshape(shape)

    # Element-wise product
    prod_mat_1d = [mat1_1d[i] * mat2_1d[i] for i in range(len(mat1_1d))]
    prod_mat = np.array(prod_mat_1d).reshape(shape)

    # Element-wise quotient
    quo_mat_1d = [mat1_1d[i] / mat2_1d[i] for i in range(len(mat1_1d))]
    quo_mat = np.array(quo_mat_1d).reshape(shape)

    return sum_mat, diff_mat, prod_mat, quo_mat
