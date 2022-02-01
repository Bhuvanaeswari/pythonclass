from pymysql import *
db=connect(host="localhost",user="root",password="",database="Directory")
#qry="create table Direct(accountno int(9) not null,accountname varchar(30) not null,bankname varchar(40) not null,ifsccode text not null,branch text not null)"
qry="alter table Direct add primary key(accountno)"
cur=db.cursor()
cur.execute(qry)
db.close()
print("tbles creted")
