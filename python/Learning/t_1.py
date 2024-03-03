import numpy as np
import tensorflow as tf

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0])
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0])

tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

