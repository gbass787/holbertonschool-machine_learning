#!/usr/bin/env python3
"""
Shuffle the data points in two matrices the same way.
"""
import numpy as np
"""
docuemnted ;;;
"""


def shuffle_data(X, Y):
    """
    Shuffle the data points in two matrices the same way.

    Args:
    X (numpy.ndarray): The first matrix of shape (m, nx) to shuffle,
                       where m is the number of data points and nx is
                       the number of features in X.
    Y (numpy.ndarray): The second matrix of shape (m, ny) to shuffle,
                       where m is the same number of data points as in X
                       and ny is the number of features in Y.

    Returns:
    numpy.ndarray, numpy.ndarray: The shuffled X and Y matrices.
    """
    assert X.shape[0] == Y.shape[0],

    perm = np.random.permutation(X.shape[0])
    shuffled_X = X[perm]
    shuffled_Y = Y[perm]

    return shuffled_X, shuffled_Y
