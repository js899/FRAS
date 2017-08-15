import numpy as np
import cv2
from tqdm import tqdm
import face_recognition
import os, os.path
import pickle

path = "./Images"


faces = []

for img in tqdm(os.listdir(path)):
	file_name = os.path.splitext(img)[0].split(' ')[0]
	img_file = cv2.imread(os.path.join(path,img))

	face_location = face_recognition.face_locations(img_file)[0]
	face_encoding = face_recognition.face_encodings(img_file)[0]
	
	faces.append([face_encoding, file_name])

print len(faces)

with open("faces.pkl", "wb") as file:
	pickle.dump(faces,file)

	
