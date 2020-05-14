from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications import imagenet_utils
import numpy as np
import imutils
import cv2
import os
import json
# internal import
from .pyimagesearch.gradcam import GradCAM
from config import UPLOAD_FOLDER

# load model
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
IMAGENET_CLASS = {}
with open(dir_path + 'imagenet_class_index.json') as json_file:
    IMAGENET_CLASS = json.load(json_file)
model = ResNet50(weights=dir_path + "resnet50_weights_tf_dim_ordering_tf_kernels.h5")

def create_resnet_gradcam(filename):
    filename = UPLOAD_FOLDER + filename
    print(filename)
    orig = cv2.imread(filename)
    resized = cv2.resize(orig, (224, 224))
    image = load_img(filename, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    preds = model.predict(image)
    i = np.argmax(preds[0])
    prob = preds[0][i]
    imagenetID, label = IMAGENET_CLASS[str(i)]
    label = "{}: {:.2f}%".format(label, prob * 100)
    print("[INFO] {}".format(label))
    cam = GradCAM(model, i)
    heatmap = cam.compute_heatmap(image)
    heatmap = cv2.resize(heatmap, (orig.shape[1], orig.shape[0]))
    (heatmap, output) = cam.overlay_heatmap(heatmap, orig, alpha=0.5)
    cv2.rectangle(output, (0, 0), (340, 40), (0, 0, 0), -1)
    # cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    output = np.hstack([orig, heatmap, output])
    output = imutils.resize(output, height=700)
    output_fname = "IMAGE_NAME.png"
    cv2.imwrite(UPLOAD_FOLDER + output_fname, output)
    return output_fname, label
