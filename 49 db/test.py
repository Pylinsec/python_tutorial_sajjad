import sqlite3

db = sqlite3.connect('people.db')
data = db.execute('select * from qoli')
# for i in data.description:
#    print(i[0])

db.execute("""INSERT INTO qoli (name,birthdate,email,country,phonenumber,job,username,password)
           values('sajjad ansaryan','1200','a@.gom','iran','123','Democratic`_Republic','sajjad' ,'123')""")
db.commit()