import sqlite3

# connect to database
db = sqlite3.connect('chinook.db')
# read information or data 

# ---------------------format1 select * --> hame chiz------------------------
# data = db.execute("SELECT * FROM name_table")

data = db.execute("SELECT * FROM customers")
# how to get column name from table 
for column in data.description:
    print(column[0])
# data = list(data)
# # data_fetch =data.fetchall()
# print(len(data_fetch))

# for line in data:
#     print(line[0],line[1])
# format 2 -->  data = db.execute("SELECT column1,column2 , column3,...  FROM name_table)")
# data = db.execute("SELECT FirstName FROM customers") # firstname
#data = db.execute("SELECT FirstName , LastName ,  FROM customers") #firstname , lastname
# data = db.execute("SELECT FirstName , LastName ,City  FROM customers") #firstname , lastname , city
data = db.execute("SELECT FirstName , LastName ,City , Country  FROM customers") #firstname , lastname , city ,country
# data_tuple = tuple(data)
data_tuple = list(data)
for item in data_tuple:
    # print(item)
    print(f"{item[0]} {item[1]} -->{item[2]} --> {item[3]}")
