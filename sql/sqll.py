# JOINing datafrom multiple tables - cleanup

import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	c.execute("SELECT populations.city, populations.population, regions.region\
		FROM populations, regions WHERE populations.city = regions.city ORDER BY\
		populations.city ASC")

	rows = c.fetchall()

	# for row in rows:
	#	print row[0], row[1], row[2]

	for row in rows:
		print "City: ", row[0]
		print "Population: ", str(row[1])
		print "Region: ", row[2]
		print