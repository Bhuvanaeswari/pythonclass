from pymysql import *
db=connect(host="localhost",user="root",password="",database="consoleversion")
#qry="create table corp(shortform varchar(100) not null,org varchar(250) not null,nature varchar(250) not null,opennings text not null,place text not null,employees int(8) not null,BasicSalary float not null,ratings float not null)"
qry="alter table corp add primary key(shortform)"

cur=db.cursor()
cur.execute(qry)
db.close()
print("tbles creted")
