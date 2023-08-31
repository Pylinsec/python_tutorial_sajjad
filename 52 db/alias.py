import sqlite3

# connect to db
db = sqlite3.connect('ketabkhaneh.db')
col_name = db.execute("SELECT * FROM person").description
# for col in col_name:
#     print(col[0],end=' ')
# onvan sootoon: id name lname book_id date
# alias --> name mostar --> table , sootoon
data = db.execute("SELECT name AS n FROM person AS p").fetchall()
data = db.execute("SELECT name FROM person AS p").fetchall()
data = db.execute("SELECT person.name , book.writer_name FROM person , book").fetchall()
data = db.execute("SELECT person.name , book.name FROM person , book ").fetchall()
data = db.execute("SELECT p.name , b.name FROM person AS p , book AS b ").fetchall()
print(data)
