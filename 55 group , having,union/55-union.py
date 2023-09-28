
import sqlite3

db= sqlite3.connect('union.db')

# union --> TEKRAR HAZF MIKONE, UNITON ALL --> hamera miarehg 
# shoroot : 1--> data type bayad ein ham bashad
# 2--> ORDER  bayad ein ham bashe
#3 ---> tedad sootoon ha moshavi bashasd
data = db.execute("""
SELECT name ,age FROM t1 
UNION 
SELECT name ,age FROM t3 ORDER BY name

""").fetchall()
print(data)
