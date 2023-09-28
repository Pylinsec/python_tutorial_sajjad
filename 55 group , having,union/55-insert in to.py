              
              
import sqlite3

# INSERT INTO table_name (col1,col2,..) --> agar bekhahim bazi sootoom haye dakhel yek table digi bereaim az in estefadeh mikonim
db= sqlite3.connect('chinook.db')
db.execute("""INSERT INTO qoli2  SELECT count(country),country
                  FROM customers
                  GROUP BY country
                  ORDER BY count(country) DESC""").fetchall()
db.commit()
data2 = db.execute("""SELECT * FROM qoli2""").fetchall()
print(data2)