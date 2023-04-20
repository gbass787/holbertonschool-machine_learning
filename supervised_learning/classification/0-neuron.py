#!/usr/bin/env python3
"""
Module for Neuron class
"""

import numpy as np


class Neuron:
    """
    Class that defines a single neuron performing binary classification
    """
    def __init__(self, nx):
        """
        Constructor method for Neuron class
        Args:
            nx (int): The number of input features to the neuron
        Attributes:
            W (numpy.ndarray): The weights vector for the neuron
            b (float): The bias for the neuron
            A (float): The activated output of the neuron (prediction)
        Raises:
            TypeError: If nx is not an integer
            ValueError: If nx is less than 1
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")
        else:
            self.W = np.random.normal(size=nx)
            self.b = 0
            self.A = 0
