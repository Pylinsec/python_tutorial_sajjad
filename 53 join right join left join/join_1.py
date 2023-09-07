import sqlite3

db = sqlite3.connect('machine.db')
# inner join ya join
data = db.execute("SELECT * FROM car join factory").fetchall()
# data = db.execute("SELECT car_name,factory_city FROM car join factory").fetchall()
#inner join  on  ,ya join on
data = db.execute("SELECT * FROM car as c  join factory as f on c.factory_name = f.name").fetchall()
print(data)