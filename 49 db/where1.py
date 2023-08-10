import sqlite3

class App():
    def __init__(self):
        self.db = sqlite3.connect('chinook.db')
        # print('connect to database was successfully')
        # self.select1()
        # self.select2()
        # self.select_distinct()
        self.select_where()


# sakhtan tabe beraye print kol dade haye dakhel databasse 
    def select1(self):
        data = self.db.execute("SELECT * FROM customers").fetchall()
        print(data)

# print sootoon hye khas 
    def select2(self):
        data = self.db.execute("SELECT City , Country, Email FROM customers").fetchall()
        for row in data:
            print(f"city-->{row[0]},country-->{row[1]},email-->{row[2]}")

# distinct --> hazf tekrar 
    def select_distinct(self):
        data = self.db.execute("SELECT DISTINCT Country FROM customers").fetchall()
        print(data)

# where ya gozashtan shart : =,!= , < <= > >= ,or , and , not ,between,like in , not in , null , not null
    def select_where(self):
        # data = self.db.execute("SELECT city FROM customers WHERE country='Canada'").fetchall()
        # data = self.db.execute("SELECT Firstname ,Lastname FROM customers WHERE country='Canada'").fetchall()
        # data = self.db.execute("SELECT Firstname ,Lastname FROM customers WHERE country!='Canada'").fetchall()
        # data = self.db.execute("SELECT Firstname ,Lastname FROM customers WHERE country in('Canada','Brezil')").fetchall()
        data = self.db.execute("SELECT Firstname ,Lastname FROM customers WHERE country not in('Canada','Brezil')").fetchall()
        print(data)





a = App
a()       
