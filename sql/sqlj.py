# create table 'regions' and populate it with data

import sqlite3

with sqlite3.connect("new.db") as conn:
	
	crs = conn.cursor()

	crs.execute("CREATE table regions (city TEXT, region TEXT)")

	cities = [
	('New York City', 'Northeast'),
    ('San Francisco', 'West'),
	('Chicago', 'Midwest'),
	('Houston', 'South'),
	('Phoenix', 'West'),
	('Boston', 'Northeast'),
	('Los Angeles', 'West'),
	('Houston', 'South'),
	('Philadelphia', 'Northeast'),
	('San Antonio', 'South'),
	('San Diego', 'West'),
	('Dallas', 'South'),
	('San Jose', 'West'),
	('Jacksonville', 'South'),
	('Indianapolis', 'Midwest'),
	('Austin', 'South'),
	('Detroit', 'Midwest')
	]

	crs.executemany("INSERT into regions VALUES (?,?)", cities)

	crs.execute("SELECT * FROM regions ORDER BY region ASC")

	rows = crs.fetchall()

	for r in rows:
		print r[0], r[1]