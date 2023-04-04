import tensorflow as tf
from LinkedList import LinkedList
from ModelInfo import ModelInfo

image_url = input("Ingresa el link de la imagen a analizar: ")
image_path = tf.keras.utils.get_file(origin=image_url)

responses = LinkedList()

DEAFULT_PATH = "./models_saved/"

models_info = [
    ModelInfo(
        name="flower",
        model=tf.keras.models.load_model(DEAFULT_PATH + "flower_photos"),
        class_names=["daisy", "dandelion", "roses", "sunflowers", "tulips"]
    ),
    ModelInfo(
        name="animal",
        model=tf.keras.models.load_model(DEAFULT_PATH + "animal_photos"),
        class_names=["cat", "dog", "wild"]
    ),
    ModelInfo(
        name="face",
        model=tf.keras.models.load_model(DEAFULT_PATH + "face_photos"),
        class_names=["female", "male"]
    ),
    ModelInfo(
        name="thing",
        model=tf.keras.models.load_model(DEAFULT_PATH + "thing_photos"),
        class_names=["things"]
    )]

img_height = 180
img_width = 180

img = tf.keras.utils.load_img(
    image_path, target_size=(img_height, img_width)
)

img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

for model_info in models_info:
    prediction = model_info.predict(img_array)
    responses.append(prediction)
    
responses.display()