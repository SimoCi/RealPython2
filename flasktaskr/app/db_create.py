# db_create.py


import sqlite3
from config import DATABASE_PATH

# create a connection with the database specified in config
with sqlite3.connect(DATABASE_PATH) as connection:

	# get a cursor object to execute SQL commands
	c = connection.cursor() 

    # create table 'tasks'
	c.execute("""
		CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL, due_date TEXT NOT NULL, 
			priority INTEGER NOT NULL,
			status INTEGER NOT NULL)
	""")

	# insert dummy data into the table
	c.execute(
		'INSERT INTO tasks (name, due_date, priority, status)' 
		'VALUES("FInish this tutorial", "02/03/2014", 10, 1)'
		)

	c.execute(
		'INSERT INTO tasks (name, due_date, priority, status)'
		'VALUES("Finish Real Python Course 2", "02/03/2014", 10, 1)'
		)