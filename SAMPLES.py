DATA=("BHUVANA")
TYPE(DATA)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    TYPE(DATA)
NameError: name 'TYPE' is not defined
type(DATA)
<class 'str'>
DATA=123
type(DATA)
<class 'int'>
DATA=12.3
type(DATA)
<class 'float'>
DATA=("BHUVAN","MADHU","REVANTH")
type(DATA)
<class 'tuple'>
DATA=["BHUVAN","MADHU","REVANTH"]
type(DATA)
<class 'list'>
DATA={"MOTHER":"BHUVAN","DAUGHTER":"MADHU","SON":"REVANTH"}
type(DATA)
<class 'dict'>
KeyboardInterrupt
DATA=("BHUVAN","MADHU","REVANTH")
DATA[0]
'BHUVAN'
DATA[1]
'MADHU'
DATA[2]
'REVANTH'
DATA=["BHUVAN","MADHU","REVANTH"]
DATA[0]
'BHUVAN'
DATA[1]
'MADHU'
DATA[2]
'REVANTH'
DATA={"MOTHER":"BHUVAN","DAUGHTER":"MADHU","SON":"REVANTH"}
DATA[MOTHER]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    DATA[MOTHER]
NameError: name 'MOTHER' is not defined
DATA["MOTHER"]
'BHUVAN'
DATA[DAUGHTER]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    DATA[DAUGHTER]
NameError: name 'DAUGHTER' is not defined
DATA["DAUGHTER"]
'MADHU'
DATA["SON"]
'REVANTH'
DATA[0]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    DATA[0]
KeyError: 0
DATA={"FAMILY":("MOTHER","DAUGHTER","SON"),"DAUGHTER":["MADHU","SREEYA","SNEKA"],"SON":{1:"REVANTH",2:"NANDHA",3:"RITHU"}}
DATA[1]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    DATA[1]
KeyError: 1
DATA["FAMILY"]
('MOTHER', 'DAUGHTER', 'SON')
DATA["FAMILY"][0:1]
('MOTHER',)
DATA["FAMILY"][2]
'SON'
DATA["DAUGHTER"]
['MADHU', 'SREEYA', 'SNEKA']
DATA["DAUGHTER"][3]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    DATA["DAUGHTER"][3]
IndexError: list index out of range
DATA["DAUGHTER"][2]
'SNEKA'
DATA["SON"]
{1: 'REVANTH', 2: 'NANDHA', 3: 'RITHU'}
DATA["SON"][1]
'REVANTH'
DATA["SON"][0]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    DATA["SON"][0]
KeyError: 0
DATA["SON"][2]
'NANDHA'
DATA[0]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    DATA[0]
KeyError: 0
DATA["SON"][3]
'RITHU'
