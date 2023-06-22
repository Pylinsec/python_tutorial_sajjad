import sqlite3

def read_data():
    db = sqlite3.connect('school.db')
    # data = db.execute("select * from dars")
    data = db.execute("select name ,year ,page from dars")
    for line in data:
        print(line)


db = sqlite3.connect('store.db')
# db.execute(" CREATE TABLE kala (id INT PRIMARY KEY NOT NULL,name TEXT,color TEXT)") # beraye bar aval miad tabel misazad vali agar table ba oon name dar db bashad error mide
db.execute(" CREATE TABLE if not exists kala (id INT PRIMARY KEY NOT NULL,name TEXT,color TEXT)")
# rahkar rafe error --> if not exists
# db.execute("INSERT INTO kala (id , name , color)  values(1,'mobile','black')")
db.execute("INSERT INTO kala  values(2,'tablet','pink')")
db.commit()