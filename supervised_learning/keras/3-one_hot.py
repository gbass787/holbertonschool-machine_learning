#!/usr/bin/env python3
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    Function that converts a label vector into a one-hot matrix

    Args:
    labels: label vector
    classes: the total number of classes

    Returns:
    one_hot_matrix: the one-hot matrix
    """
    one_hot_matrix = K.utils.to_categorical(labels, num_classes=classes)
    return one_hot_matrix
