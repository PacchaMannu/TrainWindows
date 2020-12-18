import mysql.connector
import environment as E
import datetime as D

def Time():
    tim=D.datetime.now()                                              #Get Time
    print('Time: ',tim)
    return tim

def Query():
    con=mysql.connector.connect(user='devganesh',                     #Send Query
                            password='stilldev',
                            host=E.host,
                            port=3306,
                            database='devsample')
    curs=con.cursor()
    curs.execute("SELECT * FROM EMPLOYEE")
    res=curs.fetchall()
    for i in res:
        print(i)
    con.close()    
    
def Duration(tim1,tim):
    print('Duration: ',tim1-tim)                                      #Find time difference

t=Time()
Query()
t1=Time()
Duration(t1,t)