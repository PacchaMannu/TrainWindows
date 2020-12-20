import mysql.connector
import environment as E
from datetime import datetime
import json
from os import system, name

# Establishing Connection To MySql Server
con=mysql.connector.connect(user='devganesh',    
        password='stilldev',
        host=E.host,
        port=3306,
        database='devsample')
curs=con.cursor(dictionary=True)

def clear():
    """Clearing The Screen"""
    if name == 'nt': 
        _ = system('cls')
    else: 
        _ = system('clear')

def outSql(print_table, userId):
    """Printing Output From Sql"""
    ID = {
        'userId': userId
    }
    curs.execute(print_table, ID)
    res = curs.fetchall()
    jres=json.dumps(res,default=str,indent=4)
    print(jres)

def addStu():
    """Insert Student Data Into STUDENT"""
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
    """Insert Company Data Into COMPANY"""
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
    """Insert Placement Data Into PLACEMENTS"""
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

def outStu():
    """Get Student Data Using ID"""
    userId = input("Enter Student ID: ")
    print_table = ("SELECT * FROM STUDENT WHERE ID=%(userId)s")
    outSql(print_table, userId)

def outCom():
    """Get Company Data Using ID"""
    userId = input("Enter Company ID: ")
    print_table = ("SELECT * FROM COMPANY WHERE ID=%(userId)s")
    outSql(print_table, userId)

def outDept():
    """Get Students In Specified Department"""
    userId = input("Enter Department: ")
    print_table = ("SELECT * FROM STUDENT WHERE DEPT=%(userId)s")
    outSql(print_table, userId)

def program():
    """Main Program"""
    flag='y'
    while flag == 'y':
        clear()
        inp = 0
        print("1. Add Student\n"
                "2. Add Company\n"
                "3. Update Student\n"
                "4. Update Company\n"
                "5. Display Students in Department\n"
                "6. Add Placement Details\n"
                "7. Display Student Data\n"
                "8. Display Company Data\n")
        while inp<1 or inp>8:
            inp = int(input("Enter choice: "))
            if inp<1 or inp>8:
                print("\nInvalid Choice. Enter Again\n")
        clear()
        if inp == 1:
            print("\t\tADD STUDENT\n\t\t--- -------\n")
            addStu()
        elif inp == 2:
            print("\t\tADD COMPANY\n\t\t--- -------\n")
            addEmp()
        elif inp == 3:
            pass
        elif inp == 4:
            pass
        elif inp == 5:
            print("\t\tDEPARTMENT STUDENTS\n\t\t---------- --------\n")
            outDept()
        elif inp == 6:
            print("\t\tADD PLACEMENT\n\t\t--- ---------\n")
            addPlace()
        elif inp == 7:
            print("\t\tDISPLAY STUDENT\n\t\t------- -------\n")
            outStu()
        elif inp == 8:
            print("\t\tDISPLAY COMPANY\n\t\t------- -------\n")
            outCom()
        flag = input("Do you want to run again?(y): ")

program()
con.close()