import mysql.connector
import environment as E
import datetime as D
import json

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
    curs=con.cursor(dictionary=True)
    curs.execute("SELECT * FROM EMP_ACTIVE_DATE")
    res=curs.fetchall()
    jres=json.dumps(res,default=str,indent=4)
    print("res type:",type(res[1]))
    print("json type:",type(jres))
    print(jres)
    #for i in res:
    #    print(i)
    con.close()    
    
def Duration(tim1,tim):
    print('Duration: ',tim1-tim)                                      #Find time difference

t=Time()
Query()
t1=Time()
Duration(t1,t)