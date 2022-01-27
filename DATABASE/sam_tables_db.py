from pymysql import *
db=connect(host="localhost",user="root",password="",database="newdatabase")
#qry="create table students(ROLLNO int(5) not null,NAME varchar(20) not null,ENGLISH int(3) not null,TAMIL int(3) not null,GRADE text not null)"
qry="alter table students add primary key(ROLLNO)"
cur=db.cursor()
cur.execute(qry)
db.close()
print("table created")

