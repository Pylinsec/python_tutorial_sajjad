import sqlite3

db = sqlite3.connect('machine.db')
# join tb1 ,tb2
data = db.execute("SELECT * FROM tb1 JOIN tb2").fetchall()
data = db.execute("SELECT * FROM tb1 inner JOIN tb3 on tb1.B = tb3.B").fetchall()
# tbl1 INNER JOIN YA JOIN tbl2 ON COL1 = COL2
data = db.execute("SELECT tb1.A , tb3.C FROM tb1 JOIN tb3 on tb1.B = tb3.B").fetchall()
# LEFT JOIN ---> mesl innterjoin hast ba in tefavot ke satr haye tble 1 miare vali bejaye tbl3 none mizare 
data = db.execute("SELECT * FROM tb1 LEFT JOIN tb3 on tb1.B = tb3.B").fetchall()
data = db.execute("SELECT * FROM tb1 RIGHT JOIN tb3 on tb1.B = tb3.B").fetchall()
print(data)