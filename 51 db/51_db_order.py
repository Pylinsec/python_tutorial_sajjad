import sqlite3 

# connect to db
db = sqlite3.connect('student.db')
data = db.execute(" SELECT payani1 FROM dars")
# ASCENDING  moratab bar asas koochak be  , DESENDING nozooli --> ASC , DESc
data = db.execute(" SELECT payani1 FROM dars ORDER BY payani1 ASC LIMIT 9").fetchall() #avardan 9 ta adad koochak aval list soodio
data = db.execute(" SELECT payani1 FROM dars ORDER BY payani1 DESC LIMIT 9").fetchall() # avardan 9 taye aval list noozooli 
for i in data:
    print(i,end=' ')