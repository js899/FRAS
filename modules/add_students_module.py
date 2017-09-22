import sqlite3
import datetime
import os

sem = {"I" : 1,"II" : 2,"III" : 3,"IV" : 4,"V" : 5,"VI" : 6,"VII" : 7,"VIII" : 8}

def get_year(semester):
    curr_year = datetime.datetime.today().year
    s = sem[semester]
    return str(curr_year-s/2)

def asm():
    db = sqlite3.connect(os.path.join("./databases",'students.db'))

    stud = db.cursor()


    branch = raw_input("Branch (CS,EE,EC,CE,MM,ME) : ")
    semester = raw_input("Enter Semester (I,II,III,IV,V,VI,VII,VIII): ")
    ns = int(raw_input("Number of Students : "))
    query = "CREATE TABLE {} (RegNo TEXT)".format(branch+"_"+semester)
    try:
        stud.execute(query)
        for i in range(1,ns+1):
        	insert_query = "INSERT INTO {} VALUES(?)".format(branch+"_"+semester)
        	z=""
        	if(i//10==0):
        		z="00"+str(i)
        	else:
        		z="0"+str(i)
        	stud.execute(insert_query, (get_year(semester)+"UG"+branch+ z,))
        db.commit()
        print "Entered {} students.".format(ns)
        print "Enter any key to go back to main menu."
        raw_input()
    except:
        print "Data already exixts"
        print "Enter any key to go back to main menu."
        raw_input()
    return
