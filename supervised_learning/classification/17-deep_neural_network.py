#!/usr/bin/env python3
"""
Deep neural network module
"""

import numpy as np


class DeepNeuralNetwork:
    """
    Class that defines a deep neural network performing binary classification
    """

    def __init__(self, nx, layers):
        """
        Class constructor
        @nx: Integer representing the number of input features
        @layers: List containing the number of nodes in each layer of
the network
            If nx is not an integer, raise a TypeError with the exception:
                "nx must be an integer"
            If nx is less than 1, raise a ValueError with the exception:
                "nx must be a positive integer"
            If layers is not a list or its elements are not all
positive integers,
            raise a TypeError with the exception:
                "layers must be a list of positive integers"
            Sets the private instance attributes:
            - __L: The number of layers in the neural network.
            - __cache: A dictionary to hold all intermediary values of
the network
            - __weights: A dictionary to hold all weights and biases of
the network
            Each private attribute should have a corresponding getter function
(no setter function).
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) < 1:
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for idx in range(self.__L):
            if not isinstance(layers[idx], int) or layers[idx] < 1:
                raise TypeError("layers must be a list of positive integers")
            self.__weights["b{}".format(idx + 1)] = np.zeros((layers[idx], 1))
            if idx == 0:
                Heetal = np.random.randn(layers[idx], nx) * np.sqrt(2 / nx)
                self.__weights["W{}".format(idx + 1)] = Heetal
            else:
                Heetal = np.random.randn(layers[idx], layers[idx - 1]) * \
                         np.sqrt(2 / layers[idx - 1])
                self.__weights["W{}".format(idx + 1)] = Heetal

    @property
    def L(self):
        """ Getter function for L """
        return self.__L

    @property
    def cache(self):
        """ Getter function for cache """
        return self.__cache

    @property
    def weights(self):
        """ Getter function for weights """
        return self.__weights
