import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text not null, password text not null)"
cursor.execute(create_table)
connection.commit()
connection.close()
