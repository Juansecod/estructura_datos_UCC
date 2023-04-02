from Model import Model

flowers_model = Model("flower_photos","https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz")
flowers_model.compile()
flowers_model.train()
flowers_model.save()