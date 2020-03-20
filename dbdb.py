import sqlite3

connect = sqlite3.connect('database.db')

cursor = connect.cursor()

query = """
create table IF NOT EXISTS students (
    id integer PRIMARY KEY AUTOINCREMENT,
    fio text
)
"""

cursor.execute(query)

ls = ['nonam']


query = "insert into students (fio) values (?)"
cursor.execute(query, ls)

connect.commit()
connect.close()