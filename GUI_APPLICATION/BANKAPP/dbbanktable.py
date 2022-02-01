from pymysql import *

db=connect(host="localhost",user="root",password="",database="bank")
#qry="create table banktable(accountno int(9) not null,accountname varchar(30) not null,bankname varchar(40) not null,ifsccode text not null,branch text not null,currentbal float not null,pinnum int(4) not null)"
qry ="alter table banktable add primary key(accountno)"
cur=db.cursor()
cur.execute(qry)
db.close()
print("tables created")