#!/usr/bin/env python3
import numpy as np


def normalize(X, m, s):
    """
    Normalize (standardize) a matrix.

    Args:
    X (numpy.ndarray): A matrix of shape (d, nx) to normalize,
                       where d is the number of data points and nx is
                       the number of features.
    m (numpy.ndarray): A vector of shape (nx,) containing the mean of
                       all features of X.
    s (numpy.ndarray): A vector of shape (nx,) containing the standard
                       deviation of all features of X.

    Returns:
    numpy.ndarray: The normalized X matrix.
    """
    normalized_X = (X - m) / s

    return normalized_X
