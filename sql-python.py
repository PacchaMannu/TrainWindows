import mysql.connector
import environment as E
import datetime as D

con=mysql.connector.connect(user='devganesh',                     #Send Query
    password='stilldev',
    host=E.host,
    port=3306,
    database='devsample')
curs=con.cursor()
    
def addStu():
    stuId=curs.lastrowid
    stuName = input("Enter Student name: ")
    stuDept = input("Enter Student department: ")
    stuCGPA = input("Enter Student CGPA: ")
    add_stu = {
        'stuId': stuId,
        'stuName': stuName,
        'stuDept': stuDept,
        'stuCGPA': stuCGPA
    }
    



con.close()