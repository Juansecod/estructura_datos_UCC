import tensorflow as tf
import numpy as np

class ModelInfo:
    def __init__(self, name, model, class_names):
        self.name = name
        self.model = model
        self.class_names = class_names

    def predict(self, img_array):
        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        percent_confidence = 100 * np.max(score)

        if percent_confidence > 95:
            return f"This image most likely belongs to {self.class_names[np.argmax(score)]} with a {percent_confidence:.2f} percent confidence."
        else:
            return f"This image doesn't have {self.name}"