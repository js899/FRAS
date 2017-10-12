import cv2
import face_recognition
import pickle
import operator
import numpy as np
import datetime as dt
import mark_attendance_module
import os

def attendance(semester, branch):

    try:
        loc = os.path.join("./students",branch+"_"+semester+".pkl")
        students = np.array(pickle.load(open(loc, "rb")))
    except:
        print "Unable to load student image details."
        print "Please make sure that it exists in students folder."
        return set()

    student_encodings = []
    for student in students:
    	student_encodings.append(student[0])
    face_locations = []
    cap = cv2.VideoCapture(0)
    present = []
    while(1):
    	ret,frame = cap.read()

    	frame = cv2.flip(frame,1)
    	frame = cv2.copyMakeBorder(frame,0,0,150,0,cv2.BORDER_CONSTANT,value=[0,0,0])

    	small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)

    	faces = []

    	face_locations = face_recognition.face_locations(small_frame)
    	face_encodings  = face_recognition.face_encodings(small_frame, face_locations)

    	for face_en in face_encodings:
    		distances = face_recognition.face_distance(student_encodings,face_en)
    		index, value = min(enumerate(distances), key=operator.itemgetter(1))
    		if(value<=0.47):
    		    faces.append(students[index][1])
    		    present.append(students[index][1])
    		else:
    		    faces.append("Unknown")

    	if(len(faces)>0):
    		for (top,right,bottom,left),regno in zip(face_locations, faces):
    			top = top*4
    			right = right*4
    			bottom = bottom*4
    			left = left*4

    			color = (0,0,255)

    			if (regno!="Unknown"):
    				color = (0,255,0)
    			cv2.rectangle(frame, (left,top) , (right,bottom) , color, 2)

    		y=20
    		font = cv2.FONT_HERSHEY_COMPLEX
    		for regno in faces:
    			if regno!="Unknown":
    				cv2.putText(frame, regno, (20,y), font, 0.5, (255, 255, 255), 1)
    				y = y+20

    	cv2.imshow('FRAS',frame)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
    		break

    cap.release()
    cv2.destroyAllWindows()
    return set(present)




def am():

    branch = raw_input("Enter Branch (CS,MM,ME,EC,EE,CE) : ")
    semester = raw_input("Enter Semester (I,II,III,IV,V,VI,VII,VIII) : ")

    present_students = attendance(semester, branch)
    print "\tNo of students present : {}".format(len(present_students))
    print "\tDate : ",dt.datetime.today()
    print "\tSemester : ",semester
    print "\tBranch : ",branch
    ch = str(raw_input("Do you want to mark attendance (y/n): "))
    if(ch=='y' or ch=='Y'):
        mark_attendance_module.mam(semester,branch,present_students,dt.datetime.today().day,dt.datetime.today().month,dt.datetime.today().year)
    print "Press enter to go back to main menu."
    raw_input()
    return
