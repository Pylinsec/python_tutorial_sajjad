import sqlite3

# HAVING MAX,MIN ,SUM,COUNT CONDITIN
db= sqlite3.connect('chinook.db')
data = db.execute("""SELECT  count(country),country
                  FROM customers
                  GROUP BY country
                  HAVING count(country) >=5
                  ORDER BY count(country) DESC""").fetchall()
for item in data:
    print(item)
