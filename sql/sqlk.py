# JOINING data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	c.execute("SELECT populations.city, populations.population, regions.region\
		FROM populations, regions WHERE populations.city = regions.city")

	rows = c.fetchall()

	for row in rows:
		print row[0], row[1], row[2] 