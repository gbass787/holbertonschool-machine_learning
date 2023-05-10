#!/usr/bin/env python3
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, verbose=True, shuffle=False):
    """
    Function that trains a model using mini-batch gradient descent

    Args:
    network: the model to train
    data: numpy.ndarray of shape (m, nx) containing the input data
    labels: one-hot numpy.ndarray of shape (m, classes) containing the
    labels of data
    batch_size: size of the batch used for mini-batch gradient descent
    epochs: number of passes through data for mini-batch gradient descent
    validation_data: data to validate the model with
    verbose: boolean that determines if output should be printed during
    training
    shuffle: boolean that determines whether to shuffle the
    batches every epoch

    Returns:
    history: the History object generated after training the model
    """
    history = network.fit(data, labels, epochs=epochs, batch_size=batch_size,
                          verbose=verbose, shuffle=shuffle,
                          validation_data=validation_data)
    return history
