import mysql.connector
import environment as E

con=mysql.connector.connect(user='devganesh',                     #Send Query
                            password='stilldev',
                            host=E.host,
                            port=3306,
                            database='devsample')

con.close()