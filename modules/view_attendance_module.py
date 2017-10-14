import sqlite3
import csv

def vam():
    branch = raw_input("Enter Branch (CS,EE,EC,MM,ME,CE) : ")
    semester = raw_input("Enter Semester (I,II,III,IV,V,VI,VII,VII) : ")
    month = raw_input("Enter Month (1,2,3,4,5,6,7,8,9,10,11,12) : ")
    year = raw_input("Enter Year : ")

    try :
        with sqlite3.connect("./databases/attendance.db") as connection:
            tn = branch+"_"+semester+"_"+month+"_"+year
            csvWriter = csv.writer(open("./attendances/"+tn+".csv", "w"))
            c = connection.cursor()
            c.execute("SELECT * FROM {}".format(tn))
            csvWriter.writerow([d[0] for d in c.description])
            rows = c.fetchall()
            csvWriter.writerows(rows)
        print "Find required attendance at /attendances/"+branch+"_"+semester+"_"+month+"_"+year+".csv"
    except:
        print "Could not find attendance datails for given query"
    print "Press enter to go back to main menu."
    raw_input()
    return
