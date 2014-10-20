# UPDATE and DELETE statements

import sqlite3

with sqlite3.connect("new.db") as conn:
	crs = conn.cursor()

	# update data by executing the UPDATE statement
	crs.execute("UPDATE populations SET population = 9000000 where city = 'New York City'")

	# delete specif records from table 'population' running the DELETE statement
	crs.execute("DELETE from populations WHERE city = 'Boston'")

	print "\nNew Data:\n"

	# Let's run the SELECT statement to get the updated population table
	crs.execute("SELECT * from populations")

	rows = crs.fetchall()

	# print city, state, population, row by row
	for row in rows:
		print row[0], row[1], row[2]