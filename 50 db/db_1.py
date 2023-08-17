import sqlite3
import csv


class App:
    def __init__(self):
        # self.read_from_csv()
        self.create_db()
        # self.insert_info()
        # self.read_from_db()
        self.read_from_db_like()


# read information from csv file 
    def read_from_csv(self):
        self.temp =''
        with open('student.csv','r') as file:
            read = list(csv.reader(file))
            self.column_name = read[0]
            self.info = read[1:]
            # print(str(self.column_name))
            # print(' TEXT ,'.join(self.column_name))
            for i in self.column_name:
                self.temp += i+ ' TEXT , '
            self.new_column_name = str(self.temp[:-2])


# sahkth data base , table 

    def create_db(self):
        # sakht database
        self.db = sqlite3.connect('student.db')
        # sakht table dars
        self.db.execute("CREATE TABLE if not exists dars('namedars' TEXT , 'mostmar1' TEXT , 'payani1' TEXT ,'mostamar2' TEXT , 'payan2' TEXT)")

# sakht function jehat save data dar db
    def insert_info(self):
        for row in self.info:
            self.db.execute(f"INSERT INTO dars values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}')")
            self.db.commit()
# read data
    def read_from_db(self):
        # data = self.db.execute("SELECT * FROM dars").fetchall() # hame ra miare  
        data = self.db.execute("SELECT namedars,payan2 FROM dars").fetchall() # fehgat sootoon namnedars , payan2
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1=13").fetchall() # check equal
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1 >= 13").fetchall() # check greathe equal
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1 > 13").fetchall() # check greathe 
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1 <= 13").fetchall() # check less equal  
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1 < 13").fetchall() # check less
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1 <> 13 ").fetchall() # check not equal
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1 between 13 and 17 ").fetchall() # check range n and m
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1 IN (10,13,19)").fetchall() # check agar dakhel tuple bood
        data = self.db.execute("SELECT namedars,payan2 ,payani1 FROM dars WHERE payani1 NOT IN (10,13,19)").fetchall() # check agar dakhel tuple nabood

        for satr in data:
            print(satr)



# read data with like
    def read_from_db_like(self):
        data = self.db.execute("SELECT namedars,payan2 FROM dars WHERE namedars like 'a%'").fetchall() # % har chizi bashe
        data = self.db.execute("SELECT namedars,payan2 FROM dars WHERE namedars like '%i'").fetchall() # % har akhar i bashad 
        data = self.db.execute("SELECT namedars,payan2 FROM dars WHERE namedars like 'r%i'").fetchall() # % harf avval r and  akhar i bashad 
        data = self.db.execute("SELECT namedars,payan2 FROM dars WHERE namedars like 'ria%i'").fetchall() #
        data = self.db.execute("SELECT namedars,payan2 FROM dars WHERE namedars like 'a____'").fetchall() #_ nemayande 1 harf hast
        data = self.db.execute("SELECT namedars,payan2 FROM dars WHERE namedars IS NULL").fetchall() #null yani chizi nezarim 
        data = self.db.execute("SELECT namedars,payan2 FROM dars WHERE namedars IS NOT NULL").fetchall() 

        for satr in data:
            print(satr)






a = App()
a    