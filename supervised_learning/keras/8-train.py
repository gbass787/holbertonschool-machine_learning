#!/usr/bin/env python3
import tensorflow.keras as K
import tensorflow as tf


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1, decay_rate=1,
                save_best=False, filepath=None, verbose=True, shuffle=False):
    """
    Function that trains a model using mini-batch gradient descent, early
    stopping, learning rate decay, and model checkpointing

    Args:
    network: the model to train
    data: numpy.ndarray of shape (m, nx) containing the input data
    labels: one-hot numpy.ndarray of shape (m, classes) containing the
    labels of data
    batch_size: size of the batch used for mini-batch gradient descent
    epochs: number of passes through data for mini-batch gradient descent
    validation_data: data to validate the model with
    early_stopping: boolean that indicates whether early stopping should
    be used
    patience: the patience used for early stopping
    learning_rate_decay: boolean that indicates whether learning rate
    decay should be used
    alpha: the initial learning rate
    decay_rate: the decay rate
    save_best: boolean indicating whether to save the model after
    each epoch if it is the best
    filepath: the file path where the model should be saved
    verbose: boolean that determines if output should be printed
    during training
    shuffle: boolean that determines whether to shuffle the batches
    every epoch

    Returns:
    history: the History object generated after training the model
    """
    callbacks = []

    if validation_data and early_stopping:
        early_stop = K.callbacks.EarlyStopping(monitor='val_loss',
                                               patience=patience)
        callbacks.append(early_stop)

    if validation_data and learning_rate_decay:
        def scheduler(epoch):
            return alpha / (1 + decay_rate * epoch)
        lr_decay = K.callbacks.LearningRateScheduler(scheduler, verbose=1)
        callbacks.append(lr_decay)

    if save_best and filepath:
        checkpoint = K.callbacks.ModelCheckpoint(filepath,
                                                 monitor='val_loss',
                                                 verbose=1,
                                                 save_best_only=True,
                                                 mode='min')
        callbacks.append(checkpoint)

    history = network.fit(data, labels, epochs=epochs, batch_size=batch_size,
                          verbose=verbose, shuffle=shuffle,
                          validation_data=validation_data,
                          callbacks=callbacks)
    return history
