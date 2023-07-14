import sqlite3

db = sqlite3.connect('chinook.db')
data = db.execute("SELECT LastName ,Country, FirstName FROM customers WHERE Country='Brazil' or Country='Canada'")
print(data.fetchall())