import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential

import pathlib

""" Codigo que testea la inteligencia artificial """
model = tf.keras.models.load_model("./models_saved/flower_photos")

class_names = ["daisy","dandelion","roses","sunflowers","tulips"]

img_height = 180
img_width = 180
sunflower_url = "https://i.pinimg.com/736x/39/85/a3/3985a3260a4b32e3b4b48e21b74810da--glamour.jpg"
sunflower_path = tf.keras.utils.get_file('green_rose', origin=sunflower_url)
print(sunflower_path)
img = tf.keras.utils.load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score)))