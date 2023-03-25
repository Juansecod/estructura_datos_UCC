import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential

import pathlib

class DataSet():
    def __init__(self, dataset_url, file_name) -> None:
        data_dir = tf.keras.utils.get_file(file_name, origin=dataset_url, untar=True)
        self.data_dir = pathlib.Path(data_dir)

    def get_size(self):
        image_count = len(list(self.data_dir.glob('*/*.jpg')))
        print(image_count)

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"

flowers = DataSet(dataset_url,"flowers_photos")

flowers.get_size()










""" batch_size = 32
img_height = 180
img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names
print(class_names) """