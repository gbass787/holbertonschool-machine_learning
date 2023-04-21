#!/usr/bin/env python3
"""
One-hot decoder module
"""

import numpy as np


def one_hot_decode(one_hot):
    """
    Converts a one-hot matrix into a vector of labels
    one_hot is a one-hot encoded numpy.ndarray with shape (classes, m)
        classes is the maximum number of classes
        m is the number of examples
    Returns: a numpy.ndarray with shape (m, ) containing the numeric
    labels for each example, or None on failure
    """
    if not isinstance(one_hot, np.ndarray) or len(one_hot.shape) != 2:
        return None
    if not np.all((one_hot == 0) | (one_hot == 1)):
        return None
    if not np.any(one_hot == 1):
        return None
    return np.argmax(one_hot, axis=0)
