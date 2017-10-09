import numpy as np
import cv2
from tqdm import tqdm
import face_recognition
import os, os.path
import pickle
'''
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
'''

def itp():
	path = os.path.join("", "./Image_data")
	path = os.path.abspath(os.path.realpath(path))
	branch = raw_input("Branch (CS,EE,EC,CE,MM,ME) : ")
	path = path + "/" + branch
	semester = raw_input("Enter Semester (I,II,III,IV,V,VI,VII,VIII): ")
	path = path + "/" + semester

	faces = []

	for img in tqdm(os.listdir(path)):
		file_name = os.path.splitext(img)[0].split(' ')[0]
		img_file = cv2.imread(os.path.join(path, img))

		face_location = face_recognition.face_locations(img_file)[0]
		face_encoding = face_recognition.face_encodings(img_file)[0]

		faces.append([face_encoding, file_name])

	pkl_path = os.path.join("", "./students/" + branch + "_" + semester + ".pkl")
	pkl_path = os.path.abspath(os.path.realpath(pkl_path))

	with open(pkl_path, "wb") as file:
		pickle.dump(faces, file)

	return