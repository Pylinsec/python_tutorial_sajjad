import sqlite3 

# connect to db
db = sqlite3.connect('student.db')
data = db.execute("SELECT payan2 FROM dars ORDER BY payan2 DESC ").fetchall()
data = db.execute("SELECT payan2 FROM dars ORDER BY payan2 DESC LIMIT 8").fetchall()
data = db.execute("SELECT payan2 FROM dars ORDER BY payan2 ASC LIMIT 8").fetchall()
print(data)