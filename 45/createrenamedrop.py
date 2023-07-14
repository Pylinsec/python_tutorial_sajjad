import sqlite3

# create database
# db = sqlite3.connect("C:\\Users\\classroom\\Desktop\\qoli.db")
# db = sqlite3.connect("../qoli.db") # sakht dar parent
db = sqlite3.connect("database/qoli.db")

# create table pattern
# db.execute("CREATE TABLE if not exits name (column1 INT PK,column2 TEXT,column1 TEXT , column ...)")
db.execute("CREATE TABLE if not exists info (id INT PRIMARY KEY,name TEXT,lname TEXT )")

# rename table in db
# db.execute("ALTER TABLE nameavl RENAME TO namejadid ")
# db.execute("ALTER TABLE info RENAME TO jafar ")

# drop table 
db.execute("DROP TABLE jafar")