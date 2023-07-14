import sqlite3
import os

# create db
db = sqlite3.connect('SAJJAD.db')
db.close()
os.rename('SAJJAD.db','ansaryan.db')
