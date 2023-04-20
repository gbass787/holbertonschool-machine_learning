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
        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron
        X is a numpy.ndarray with shape (nx, m) that contains the input data
        nx is the number of input features to the neuron
        m is the number of examples
        Updates the private attribute __A
        The neuron should use a sigmoid activation function
        Returns the private attribute __A
        """
        z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        Y is a numpy.ndarray with shape (1, m) that contains the correct
        labels for the input data
        A is a numpy.ndarray with shape (1, m) containing the activated
        output of the neuron for each example
        To avoid division by zero errors, please use 1.0000001 - A
        instead of 1 - A
        Returns the cost
        """
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)) / m
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron's predictions
        X is a numpy.ndarray with shape (nx, m) that contains the input data
            nx is the number of input features to the neuron
            m is the number of examples
        Y is a numpy.ndarray with shape (1, m) that contains the correct labels
            for the input data
        Returns the neuron's prediction and the cost of the network,
respectively
        The prediction should be a numpy.ndarray with shape (1, m) containing
            the predicted labels for each example
        The label values should be 1 if the output of the network
is >= 0.5 and 0 otherwise
        """
        self.__A = self.forward_prop(X)
        prediction = np.where(self.__A >= 0.5, 1, 0)
        cost = self.cost(Y, self.__A)
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neuron
        X is a numpy.ndarray with shape (nx, m) that contains the input data
            nx is the number of input features to the neuron
            m is the number of examples
        Y is a numpy.ndarray with shape (1, m) that contains the correct
            labels for the input data
        A is a numpy.ndarray with shape (1, m) containing the activated
            output of the neuron for each example
        alpha is the learning rate
        Updates the private attributes __W and __b
        """
        m = Y.shape[1]
        dz = A - Y
        dw = np.dot(X, dz.T) / m
        db = np.sum(dz) / m
        self.__W -= alpha * dw.T
        self.__b -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        Trains the neuron
        X is a numpy.ndarray with shape (nx, m) that contains the input data
            nx is the number of input features to the neuron
            m is the number of examples
        Y is a numpy.ndarray with shape (1, m) that contains
the correct labels for the input data
        iterations is the number of iterations to train over
            if iterations is not an integer, raise a TypeError with
the exception iterations must be an integer
            if iterations is not positive, raise a ValueError with
the exception iterations must be a positive integer
        alpha is the learning rate
            if alpha is not a float, raise a TypeError with the
exception alpha must be a float
            if alpha is not positive, raise a ValueError with the
exception alpha must be positive
        All exceptions should be raised in the order listed above
        Updates the private attributes __W, __b, and __A
        You are allowed to use one loop
        Returns the evaluation of the training data after iterations
of training have occurred
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 1:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            self.__A = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)

        return self.evaluate(X, Y)
