import csv , sqlite3
class App():
    def __init__(self):
        self.reader_data()
        self.make_db()

# khandan info
    def reader_data(self):
        with open('information.csv','r') as file:
            reader = csv.reader(file)
            data = list(reader)
            self.coulmn_name = data[0]
            self.data_info=data[1:]
            # for row in reader:
            #     print(row)


#  make db
    def make_db(self):
        self.db = sqlite3.connect('people.db')
        a,b,c,d,e,f,g,h=self.coulmn_name
  
        self.db.execute(f"""CREATE TABLE if not exists
                            qoli({a} TEXT,{b} TEXT,{c} TEXT,{d} TEXT,{e} TEXT,{f} TEXT,{g} TEXT,{h} TEXT)""")






a = App
a()
