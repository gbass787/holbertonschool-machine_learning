#!/usr/bin/env python3
"""
calculates the normalization constants of a matrix
"""
import numpy as np


def normalization_constants(X):
    """
    Calculate the normalization constants of a matrix.

    Args:
    X (numpy.ndarray): A matrix of shape (m, nx) to normalize
                       where m is the number of data points and nx is
 the number of features.

    Returns:
    mean (numpy.ndarray): The mean of each feature.
    std_dev (numpy.ndarray): The standard deviation of each feature.
    """
    mean = np.mean(X, axis=0)
    std_dev = np.std(X, axis=0)

    return mean, std_dev
