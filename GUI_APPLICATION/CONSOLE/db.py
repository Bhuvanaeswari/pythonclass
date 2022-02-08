from pymysql import *
db=connect(host="localhost",user="root",password="")
qry="create database consoleversion"
cur=db.cursor()
cur.execute(qry)
db.close()
print("dtbse creted")