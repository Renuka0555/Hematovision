import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("blood_model.h5")

classes = ['Eosinophil','Lymphocyte','Monocyte','Neutrophil']

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    result = model.predict(img_array)
    return classes[np.argmax(result)]
