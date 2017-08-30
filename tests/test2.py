#Create a box around the face
import cv2
import face_recognition

cap = cv2.VideoCapture(0)

while(1):
	ret,frame = cap.read()

	face_locations = face_recognition.face_locations(frame)

	for face in face_locations:
		cv2.rectangle(frame, (face[3], face[0]), (face[1], face[2]), (255,0,0), 2)

	cv2.imshow('FRAC',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()