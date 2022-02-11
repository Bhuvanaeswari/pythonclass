from pymysql import *
db=Connect(host="localhost",user="root",password="",database="Directory")
#qry ="create table directfirst(accountno int(9) not null,accountname varchar(250) not null)"
#cur=db.cursor()
#cur.execute(qry)

print("directfirst & sec creted")
#qry2 ="create table directsecond(accountno int(9) not null,bankname varchar(100) not null,ifsccode text not null,branch text not null)"
qry1="alter table directfirst add primary key(accountno)"
qry2="alter table directsecond add primary key(accountno)"

cur=db.cursor()
cur.execute(qry1)
cur.execute(qry2)
db.close()