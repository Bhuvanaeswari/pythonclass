from pymysql import *
db=connect(host="localhost",user="root",password="")
qry= "create database  newdatabase"
cur=db.cursor()
cur.execute(qry)
db.close()
print("database created")


