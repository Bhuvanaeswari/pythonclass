from pymysql import *
db=connect(host="localhost",user="root",password="")
qry="create database Bank"
cur=db.cursor()
cur.execute(qry)
db.close()
print("dtbse creted")