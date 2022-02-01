from pymysql import *
db=connect(host="localhost",user="root",password="")
qry="create database console"
cur=db.cursor()
cur.execute(qry)
db.close()
print("database1 created")
