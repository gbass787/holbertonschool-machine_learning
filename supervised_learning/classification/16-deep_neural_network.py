#!/usr/bin/env python3
""" Deep neural network module """

import numpy as np


class DeepNeuralNetwork:
    """ Class that defines a deep neural network performing binary
        classification """

    def __init__(self, nx, layers):
        """ Class constructor
            @nx: Integer representing the number of input features
            @layers: List containing the number of nodes in each layer of the
                     network

            If nx is not an integer, raise a TypeError with the exception:
                "nx must be an integer"
            If nx is less than 1, raise a ValueError with the exception:
                "nx must be a positive integer"
            If layers is not a list or its elements are not all positive
            integers, raise a TypeError with the exception:
                "layers must be a list of positive integers"

            Sets the public instance attributes:
            - L: The number of layers in the neural network.
            - cache: A dictionary to hold all intermediary values of
the network
            - weights: A dictionary to hold all weights and biased of
the network
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
        for l in range(self.L):
            if not isinstance(layers[l], int) or layers[l] < 1:
                raise TypeError("layers must be a list of positive integers")
            self.weights["b{}".format(l+1)] = np.zeros((layers[l], 1))
            if l == 0:
                Heetal = np.random.randn(layers[l], nx) * np.sqrt(2/nx)
                self.__weights["W{}".format(l+1)] = Heetal
            else:
                Heetal = np.random.randn(layers[l], layers[l-1]) * \
                         np.sqrt(2/layers[l-1])
                self.__weights["W{}".format(l+1)] = Heetal

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
