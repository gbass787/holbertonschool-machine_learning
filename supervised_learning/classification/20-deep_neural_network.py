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

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neural network
        X is a numpy.ndarray with shape (nx, m) that contains the input data
            nx is the number of input features to the neuron
            m is the number of examples
        Updates the private attribute __cache:
            The activated outputs of each layer should be saved in the __cache
dictionary using the key A{l} where {l} is the hidden layer the activated
output belongs to
            X should be saved to the cache dictionary using the key A0
        All neurons should use a sigmoid activation function
        You are allowed to use one loop
        Returns the output of the neural network and the cache, respectively
        """
        self.__cache['A0'] = X
        for layer in range(self.__L):
            weight = self.__weights['W{}'.format(layer + 1)]
            bias = self.__weights['b{}'.format(layer + 1)]
            z = np.dot(weight, self.__cache['A{}'.format(layer)]) + bias
            A = 1 / (1 + np.exp(-z))
            self.__cache['A{}'.format(layer + 1)] = A
        return self.__cache['A{}'.format(self.__L)], self.__cache

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        Y is a numpy.ndarray with shape (1, m) that contains the correct
        labels for the input data
        A is a numpy.ndarray with shape (1, m) containing the activated output
        of the neuron for each example
        To avoid division by zero errors, please use 1.0000001 - A instead
        of 1 - A
        Returns the cost
        """
        m = Y.shape[1]
        cost = (-1 / m) * np.sum(Y * np.log(A) +
                                 (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neural network’s predictions
        X is a numpy.ndarray with shape (nx, m) that contains the
input data
            nx is the number of input features to the neuron
            m is the number of examples
        Y is a numpy.ndarray with shape (1, m) that contains the
correct labels for
        the input data
        Returns the neuron’s prediction and the cost of the network,
respectively
            The prediction should be a numpy.ndarray with shape (1, m)
containing
            the predicted labels for each example
            The label values should be 1 if the output of the network is >=
0.5 and 0
            otherwise
        """
        A, self.__cache = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost
