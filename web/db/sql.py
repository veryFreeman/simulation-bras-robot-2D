import sqlite3 as sql

conn = sql.connect('db.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO user VALUES(null, "blazz@blazz.com", "blazz")')