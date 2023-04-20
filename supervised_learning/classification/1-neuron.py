#!/usr/bin/env python3
"""
Module that defines a Neuron performing binary classification
"""


import numpy as np


class Neuron:
    """
    Class that defines a single neuron performing binary classification
    """
    def __init__(self, nx):
        """
        Constructor method that initializes a Neuron instance

        Args:
            nx (int): number of input features to the neuron

        Raises:
            TypeError: if nx is not an integer
            ValueError: if nx is less than 1
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.normal(size=nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        Getter method for the weights vector of the neuron

        Returns:
            numpy.ndarray: the weights vector of the neuron
        """
        return self.__W

    @property
    def b(self):
        """
        Getter method for the bias of the neuron

        Returns:
            float: the bias of the neuron
        """
        return self.__b

    @property
    def A(self):
        """
        Getter method for the activated output of the neuron

        Returns:
            float: the activated output of the neuron
        """
        return self.__A
