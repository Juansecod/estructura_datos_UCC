from Model import Model
from os import path

model_name = "face_photos"
data_dir = path.join('C:\\Users\\juans\\.keras\\datasets',model_name)

flowers_model = Model(model_name,data_dir=data_dir)
flowers_model.compile()
flowers_model.train()
flowers_model.save()