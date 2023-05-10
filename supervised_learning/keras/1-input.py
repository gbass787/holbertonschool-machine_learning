#!/usr/bin/env python3
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Function that builds a neural network with the Keras library

    Args:
    nx: number of input features to the network
    layers: list containing the number of nodes in each layer of the network
    activations: list containing the activation functions used for each layer
    of the network
    lambtha: the L2 regularization parameter
    keep_prob: the probability that a node will be kept for dropout

    Returns:
    model: a keras model
    """

    inputs = K.Input(shape=(nx,))
    regularizer = K.regularizers.l2(lambtha)

    my_layer = K.layers.Dense(layers[0], activation=activations[0],
                              kernel_regularizer=regularizer)(inputs)
    for i in range(1, len(layers)):
        my_layer = K.layers.Dropout(1 - keep_prob)(my_layer)
        my_layer = K.layers.Dense(layers[i], activation=activations[i],
                                  kernel_regularizer=regularizer)(my_layer)

    model = K.Model(inputs=inputs, outputs=my_layer)

    return model
