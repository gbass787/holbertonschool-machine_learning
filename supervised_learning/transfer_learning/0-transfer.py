#!/usr/bin/env python3

import tensorflow.keras as K
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import img_to_array, array_to_img


def preprocess_data(X, Y):
    """
    Function to preprocess the data.
    """
    X_p = K.applications.densenet.preprocess_input(X)
    Y_p = K.utils.to_categorical(Y, 10)

    return X_p, Y_p


if __name__ == "__main__":
    """
    Main function.
    """

    # Load the CIFAR-10 data
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    # Preprocess the data
    x_train, y_train = preprocess_data(x_train, y_train)
    x_test, y_test = preprocess_data(x_test, y_test)

    # Resize data to be compatible with DenseNet121 model
    x_train = K.layers.Lambda(lambda image: K.preprocessing.image.smart_resize(image, (224, 224)))(x_train)
    x_test = K.layers.Lambda(lambda image: K.preprocessing.image.smart_resize(image, (224, 224)))(x_test)

    # Load the DenseNet121 model
    base_model = K.applications.DenseNet121(include_top=False, weights='imagenet', input_shape=(224, 224, 3))

    # Freeze the base model
    base_model.trainable = False

    # Create new model on top
    inputs = K.Input(shape=(224, 224, 3))
    x = base_model(inputs, training=False)
    x = K.layers.GlobalAveragePooling2D()(x)
    outputs = K.layers.Dense(10, activation='softmax')(x)
    model = K.Model(inputs, outputs)

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    history = model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_test, y_test))

    model.save('cifar10.h5')
