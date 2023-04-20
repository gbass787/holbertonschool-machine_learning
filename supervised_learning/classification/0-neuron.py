#!/usr/bin/env python3
"""Module that defines a single neuron performing binary classification"""

import numpy as np


class Neuron:
    """Class that defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """Class constructor for Neuron

        Args:
            nx (int): The number of input features to the neuron

        Raises:
            TypeError: If nx is not an integer
            ValueError: If nx is less than 1
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for the weights vector for the neuron"""
        return self.__W

    @property
    def b(self):
        """Getter for the bias for the neuron"""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output of the neuron (prediction)"""
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron

        Args:
            X (numpy.ndarray): The input data of shape (nx, m)

        Returns:
            numpy.ndarray: The activated output of the neuron (prediction)
        """
        z = np.matmul(self.W, X) + self.b
        self.__A = 1 / (1 + np.exp(-z))
        return self.A
