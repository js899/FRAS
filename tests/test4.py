#detecting faces

import cv2
import face_recognition
import pickle
import operator
import numpy as np

cap = cv2.VideoCapture(0)

students = np.array(pickle.load(open("faces.pkl", "rb")))

student_encodings = []
for student in students:
	student_encodings.append(student[0])

process_this_frame = True

face_locations = []


while(1):
	ret,frame = cap.read()

	frame = cv2.flip(frame,1)
	frame = cv2.copyMakeBorder(frame,0,0,100,0,cv2.BORDER_CONSTANT,value=[0,0,0])

	small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)

	#process_this_frame = True

	faces = []

	face_locations = face_recognition.face_locations(small_frame)
	face_encodings  = face_recognition.face_encodings(small_frame, face_locations)

	for face_en in face_encodings:
		distances = face_recognition.face_distance(student_encodings,face_en)
		index, value = min(enumerate(distances), key=operator.itemgetter(1))
		if(value<=0.47):
			faces.append(students[index][1])
		else:
			faces.append("Unknown")


	print len(face_encodings), len(faces)

	if(len(faces)>0):
		for (top,right,bottom,left),name in zip(face_locations, faces):
			top = top*4
			right = right*4
			bottom = bottom*4
			left = left*4

			color = (0,0,255)

			if name!="Unknown":
				color = (0,255,0)
			cv2.rectangle(frame, (left,top) , (right,bottom) , color, 2)
		
		y=20
		font = cv2.FONT_HERSHEY_COMPLEX
		for name in faces:
			if(name!="Unknown"):
				cv2.putText(frame, name, (20,y), font, 0.5, (255, 255, 255), 1)
				y = y+20

	    	

	    
	cv2.imshow('FRAS',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
