#!/usr/bin/env python3
"""
Defines a neural network with one hidden layer performing binary classification
"""

import numpy as np


class NeuralNetwork:
    """NeuralNetwork class"""

    def __init__(self, nx, nodes):
        """Instantiation method for NeuralNetwork class"""

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """Returns the value of the private attribute __W1"""
        return self.__W1

    @property
    def b1(self):
        """Returns the value of the private attribute __b1"""
        return self.__b1

    @property
    def A1(self):
        """Returns the value of the private attribute __A1"""
        return self.__A1

    @property
    def W2(self):
        """Returns the value of the private attribute __W2"""
        return self.__W2

    @property
    def b2(self):
        """Returns the value of the private attribute __b2"""
        return self.__b2

    @property
    def A2(self):
        """Returns the value of the private attribute __A2"""
        return self.__A2

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network"""

        def sigmoid(x):
            """Sigmoid activation function"""
            return 1 / (1 + np.exp(-x))

        self.__A1 = sigmoid(np.dot(self.__W1, X) + self.__b1)
        self.__A2 = sigmoid(np.dot(self.__W2, self.__A1) + self.__b2)
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""

        m = Y.shape[1]
        cost = (-1 / m) * np.sum(
            Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """Evaluates the neural network's predictions"""

        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        A2_eval = np.where(A2 >= 0.5, 1, 0)
        return A2_eval, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """Calculates one pass of gradient descent on the neural network"""

        m = Y.shape[1]
        dZ2 = A2 - Y
        dW2 = (1 / m) * np.dot(dZ2, A1.T)
        db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)
        dZ1 = np.dot(self.W2.T, dZ2) * (A1 * (1 - A1))
        dW1 = (1 / m) * np.dot(dZ1, X.T)
        db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)

        self.__W2 -= alpha * dW2
        self.__b2 -= alpha * db2
        self.__W1 -= alpha * dW1
        self.__b1 -= alpha * db1

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """Trains the neural network"""

        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 1:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            A1, A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, A1, A2, alpha)

        return self.evaluate(X, Y)
