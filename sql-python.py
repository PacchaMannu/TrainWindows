import mysql.connector
import environment as E
from datetime import datetime

con=mysql.connector.connect(user='devganesh',                     #Send Query
    password='stilldev',
    host=E.host,
    port=3306,
    database='devsample')
curs=con.cursor()
    
def addStu():
    stuId = input("Enter Student ID: ")
    stuName = input("Enter Student name: ")
    stuDept = input("Enter Student department: ")
    stuCGPA = input("Enter Student CGPA: ")
    add_stu = {
        'stuId': stuId,
        'stuName': stuName,
        'stuDept': stuDept,
        'stuCGPA': stuCGPA
    }
    add_student = ("INSERT INTO STUDENT "
                    "VALUES (%(stuId)s, %(stuName)s, %(stuDept)s, %(stuCGPA)s)")
    curs.execute(add_student, add_stu)
    con.commit()

def addEmp():
    comId = input("Enter Company ID: ")
    comName = input("Enter Company name: ")
    comLocation = input("Enter Company location: ")
    comDate = None
    while True:
        print("Enter Interview date:",end=' ')
        dat = str(input())
        try:
            comDate = datetime.strptime(dat, "%Y-%m-%d")
            break
        except:
            print("Incorrect format. Enter again")
    add_com = {
        'comId': comId,
        'comName': comName,
        'comLocation': comLocation,
        'comDate': comDate
    }
    add_company = ("INSERT INTO COMPANY "
                    "VALUES (%(comId)s, %(comName)s, %(comLocation)s, %(comDate)s)")
    curs.execute(add_company, add_com)
    con.commit()

def addPlace():
    stuId = input("Enter Student ID: ")
    comId = input("Enter Company ID: ")
    Pack = input("Enter Package: ")
    add_place = {
        'stuId': stuId,
        'comId': comId,
        'Pack': Pack
    }
    add_placement = ("INSERT INTO PLACEMENTS "
                    "VALUES (%(stuId)s, %(comId)s, %(Pack)s)")
    curs.execute(add_placement, add_place)
    con.commit()

addPlace()
con.close()