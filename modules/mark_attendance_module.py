import sqlite3
from get_days_months import *
import os

def mam(semester, branch, present_students, d, m, y):
    d,m,y = str(d),str(m),str(y)
    db1 = sqlite3.connect(os.path.join('./databases/', 'attendance.db'))
    db2 = sqlite3.connect(os.path.join('./databases/', 'students.db'))
    atten = db1.cursor()
    stud = db2.cursor()

    table_name = branch + "_" + semester + "_" + m + "_" + y
    table_exists = 'SELECT name FROM sqlite_master WHERE type="table" AND name=:t_n'
    if(not atten.execute(table_exists,{'t_n' : table_name}).fetchone()):
    	nd = get_no_of_days(int(m), int(y))
    	values = "( 'RegNo' TEXT, "
    	for i in range(1,nd+1):
    		if(i!=nd):
    			values = values + "'" + str(i) + "/" + m + "/" + y + "'" + " TEXT, "
    		else:
    			values = values + "'" + str(i) + "/" + m + "/" + y + "'" + " TEXT "
    	values = values + " ) "
    	create_table = 'CREATE TABLE {0} {1};'.format(table_name,values)
    	atten.execute(create_table)
    try:
        all_students = stud.execute('SELECT * FROM {}'.format(branch+"_"+semester)).fetchall()
    except:
        print "Student Details Missing in student database in the database folder."
        return
	for s in all_students:
		st = s[0]
		atten.execute("INSERT INTO {}('RegNo') VALUES(?)".format(table_name),(st,) )
    for regno in present_students:
        update_command = "UPDATE {} SET {} = 'P' WHERE RegNo=?".format(table_name,"'"+d+"/"+m+"/"+y+"'")
        atten.execute(update_command, (regno,))
    print "Attendance Marked."
    db1.commit()
    db2.commit()
