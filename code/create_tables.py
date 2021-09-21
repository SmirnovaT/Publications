import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE publications (id int, title text, content text)"
cursor.execute(create_table)

connection.commit()

connection.close()