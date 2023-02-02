import tensorflow as tf
from tensorflow import keras
import numpy as np


def model_local():
    model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
    model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
    return model