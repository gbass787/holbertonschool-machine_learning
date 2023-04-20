#!/usr/bin/env python3
"""
Defines a single neuron performing binary classification
"""


import numpy as np


class Neuron:
    """
    Class that defines a single neuron performing binary classification
    """

    def __init__(self, nx):
        """
        Class constructor
        Args:
            nx: Number of input features to the neuron
        """

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.normal(size=nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """ Getter function for __W """
        return self.__W

    @property
    def b(self):
        """ Getter function for __b """
        return self.__b

    @property
    def A(self):
        """ Getter function for __A """
        return self.__A
