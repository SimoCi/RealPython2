# SQL Functions

import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	#create a dictionary of sql queries
	sql = {
	'average': "SELECT avg(population) FROM populations",
	'maximum': "SELECT max(population) FROM populations",
	'minimum': 'SELECT min(population) FROM populations',
	'sum': "SELECT sum(population) FROM populations",
	'count': "SELECT count(city) FROM populations"}

	# loop through the dictionary items
	# use values to run queries
	# get result and print it using the current key
	for key, value in sql.iteritems():

		c.execute(value)

		result = c.fetchone()

		print key + ": ", result[0]