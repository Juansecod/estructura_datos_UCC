from pathlib import Path
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential

class Model:
    data_dir: Path
    model_name: str
    BATCH_SIZE = 32
    IMG_HEIGHT = 180
    IMG_WIDTH = 180
    AUTOTUNE = tf.data.AUTOTUNE
    
    def __init__(self, model_name, dataset_url = None, data_dir = None,):
        self.model_name = model_name
        if data_dir is None:
            data_dir = tf.keras.utils.get_file(model_name, origin=dataset_url, untar=True)
        self.data_dir = Path(data_dir)
        print(self.data_dir)
        
        train_ds = tf.keras.utils.image_dataset_from_directory(
            self.data_dir,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(self.IMG_HEIGHT, self.IMG_WIDTH),
            batch_size=self.BATCH_SIZE)
        
        val_ds = tf.keras.utils.image_dataset_from_directory(
            self.data_dir,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(self.IMG_HEIGHT, self.IMG_WIDTH),
            batch_size=self.BATCH_SIZE)
        
        self.class_names = train_ds.class_names
        
        self.num_classes = len(self.class_names)
        
        self.train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=self.AUTOTUNE)
        self.val_ds = val_ds.cache().prefetch(buffer_size=self.AUTOTUNE)

        self.data_augmentation = keras.Sequential(
            [
                layers.RandomFlip("horizontal",
                                input_shape=(self.IMG_HEIGHT,
                                            self.IMG_WIDTH,
                                            3)),
                layers.RandomRotation(0.1),
                layers.RandomZoom(0.1),
            ]
        )
        
        self.model = Sequential([
            self.data_augmentation,
            layers.Rescaling(1./255),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.2),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(self.num_classes, name="outputs")
        ])
    
    def compile(self):
        self.model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
        self.model.summary()
        
    def train(self):
        epochs = 15
        self.history = self.model.fit(
            self.train_ds,
            validation_data=self.val_ds,
            epochs=epochs
        )
        
    def save(self):
        model_dir = "./models_saved/" + self.model_name
        self.model.save(model_dir)