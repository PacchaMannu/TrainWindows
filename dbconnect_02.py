import mysql.connector
import environment as E
import datetime as D
import json

def Time():
    """get current time"""
    tim=D.datetime.now()                                              
    print('Time: ',tim)
    return tim

def Query():
    """running sql command"""
    con=mysql.connector.connect(user='devganesh',                    
        password='stilldev',
        host=E.host,
        port=3306,
        database='devsample')
    curs=con.cursor(dictionary=True)
    curs.execute("SELECT * FROM EMP_ACTIVE_DATE")
    res=curs.fetchall()
    jres=json.dumps(res,default=str,indent=4)
    #ult=json.loads(jres)             "json to dict"
    # for i in ult:                   
    #     print(i)

    # print("res type:",type(res[1])) "result type"
    
    # print("json type:",type(jres))  "json output type"
    
    print(jres)                     #"print json"
    
    # for i in res:                   "print result"
    #    print(i)
    con.close()    
    
def Duration(tim1,tim):
    """duration of sql command"""
    print('Duration: ',tim1-tim)                                      

t=Time()
Query()
t1=Time()
Duration(t1,t)