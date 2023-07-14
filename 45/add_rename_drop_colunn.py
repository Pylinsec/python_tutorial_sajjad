import sqlite3

db = sqlite3.connect("database/qoli.db")
db.execute("CREATE TABLE if not exists info (id INT PRIMARY KEY,name TEXT,lname TEXT )")

#  add column 
# db.execute("ALTER TABLE  نام جدولADD COLUMN نام ستون TEXT")
# db.execute("ALTER TABLE info ADD COLUMN city TEXT")

# rename columnn name 
# db.execute("ALTER TABLE info RENAME COLUMN city to country")
# DROP COLUMN 
db.execute("ALTER TABLE info DROP COLUMN COUNTRY")