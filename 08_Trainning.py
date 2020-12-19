import numpy as np
from PIL import Image
import os
import cv2


# creat file name
def train_classifier(Pic001_dir):
    path = [os.path.join(Pic001_dir, f) for f in os.listdir(Pic001_dir)]

    faces = []
    ids = []

    for image in path:
        img = Image.open(image).convert("L")
        imageNP = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
        faces.append(imageNP)
        ids.append(id)

    ids = np.array(ids)

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    # name's file
    clf.write("PersonClassifierFHA.xml")


# call function
train_classifier("Pic001")
