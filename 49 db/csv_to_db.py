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
            # print(self.data_info)
            # for row in reader:
            #     print(row)


#  make db
    def make_db(self):
        self.db = sqlite3.connect('people.db')
        a,b,c,d,e,f,g,h=self.coulmn_name
  
        self.db.execute(f"""CREATE TABLE if not exists
                            qoli({a}TEXT,{b} BLOB,{c}TEXT,{d}TEXT,{e}TEXT,{f}TEXT,{g}TEXT,{h}TEXT)""")
        for li in self.data_info:
        
                self.db.execute(f"INSERT INTO qoli values('{li[0]}','{li[1]}','{li[2]}','{li[3]}','{li[4]}','{li[5]}','{li[6]}','{li[7]}')")
                self.db.commit()





a = App
a()
