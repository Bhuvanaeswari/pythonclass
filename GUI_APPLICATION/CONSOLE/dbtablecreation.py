from pymysql import *

db=connect(host="localhost",user="root",password="",database="console")
#qry="create table corporate(org varchar(250) not null,nature varchar(250) not null,opennings text not null,place text not null,employees int(8) not null,BasicSalary float not null,ratings float not null)"
qry ="alter table corporate add primary key(org)"
cur=db.cursor()
cur.execute(qry)
db.close()
print("tables created")