import sqlite3
from get_days_months import *

'''
student = raw_input("Name : ").upper()
d,m,y = raw_input("Date (DD-MM-YYYY) : ").split("-")
branch = raw_input("Branch : ").upper()
semester = raw_input("Semester (FIRST, SECOND, ...): ")
'''
regno = "2015UGCS071"
d,m,y = "3","9","2017"
branch = "CS"
semester = "FIFTH"

db1 = sqlite3.connect('attendance.db')
db2 = sqlite3.connect('students.db')
atten = db1.cursor()
stud = db2.cursor()

print "Connected to db"

table_name = branch + "_" + semester + "_" + m + "_" + y
table_exists = 'SELECT name FROM sqlite_master WHERE type="table" AND name=:t_n'
if(atten.execute(table_exists,{'t_n' : table_name}).fetchone()):
	print "Table Exists"
else:

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
	all_students = stud.execute('SELECT * FROM {}'.format(branch+"_"+semester)).fetchall()
	for s in all_students:
		st = s[0]
		atten.execute("INSERT INTO {}('RegNo') VALUES(?)".format(table_name),(st,) )
	print "Table created"

update_command = "UPDATE {} SET {} = 'P' WHERE RegNo=?".format(table_name,"'"+d+"/"+m+"/"+y+"'")
print update_command
atten.execute(update_command, (regno,))
print "Table Updated"
db1.commit()
db2.commit()
