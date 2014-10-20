# SELECT statement - remove unicode characters

# import the sqlite3 librry
import sqlite3

# creating a connection object using the 'with' keyword
with sqlite3.connect("new.db") as conn:

	# get cursor from connection
	cursor = conn.cursor()

	cursor.execute("SELECT firstname, lastname from employees")

	# fetchall(): removes all unicode characters from the query
	# from cursor get the fetchall() function and call it with no parameters
	# assign output to variable 'rows'
	rows = cursor.fetchall()

	# for-loop over rows outputted by executing the SELECT statement to query new.db
	# iterating through table 'employees' and printing results line by line, without u characters
	for row in rows :
		print row[0], row[1]