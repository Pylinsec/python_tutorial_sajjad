import sqlite3 

# connect to db
db = sqlite3.connect('student.db')
data_all = db.execute("SELECT * FROM dars").fetchall()
data_one = db.execute("SELECT mostmar1 FROM dars").fetchall()
data_min = db.execute("SELECT MIN(mostmar1) FROM dars").fetchall()# kamtarin meqdar sotoon mostmar1 ra miareh
data_max = db.execute("SELECT MAX(mostmar1) FROM dars").fetchall() # bozorgtarin meqdar sootoon barmigardanad
data_max_WHERE = db.execute("SELECT MAX(mostmar1) FROM dars WHERE mostmar1 < 15").fetchall()
data_count = db.execute("SELECT count(mostmar1) FROM dars").fetchall() # shomaresh tedad radif dar on sootoon
data_count_where = db.execute("SELECT count(mostmar1) FROM dars WHERE mostmar1 < 15").fetchall()
data_sum = db.execute("SELECT SUM(mostmar1) FROM dars").fetchall() # mohasebe mojmoo radif ha dor sootoon khas 
data_mix = db.execute("SELECT SUM(mostmar1) , COUNT(mostmar1),MAX(mostmar1),MIN(mostmar1) FROM dars").fetchall() # mohasebe mojmoo radif ha dor sootoon khas 
data_avg = db.execute("SELECT AVG(mostmar1) FROM dars").fetchall() # gereftan miangin sootoon 

print(data)