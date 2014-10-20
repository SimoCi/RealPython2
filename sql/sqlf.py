# SELECT statement

# import the sqlite3 librry
import sqlite3

# creating a connection object using the 'with' keyword
with sqlite3.connect("new.db") as conn:

	# get cursor from connection
	cursor = conn.cursor()

	# for-loop over rows outputted by executing the SELECT statement to query new.db
	# iterating through table 'employees' and printing result line by line
	# that prints unicode strings
	for row in cursor.execute("SELECT firstname, lastname from employees"):
		print row

