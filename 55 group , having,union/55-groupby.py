import sqlite3

db= sqlite3.connect('chinook.db')
# yaftan name sarsootoon =======================================================
data = db.execute("SELECT * FROM customers").description
# for col_name in data:
#     print(col_name[0])

# khandan etelat dakhel table ======================================================

# GROUPBY =========================== groupo bandi bar asas sootoon ke behsh midim

# data = db.execute("""SELECT country 
#                   FROM customers
#                   WHERE ----  
#                   GROUPBY ---
#                   ORDER BY  """).fetchall()
#                   
data = db.execute("""SELECT  count(country),country
                  FROM customers
                  GROUP BY country
                  ORDER BY count(country) DESC""").fetchall()
for item in data:
    print(item)
