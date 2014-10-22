import sqlite3
import random

with sqlite3.connect("newnum.db") as conn:
	c = conn.cursor()

	# create table 'numbers'
	c.execute("CREATE TABLE numbers (random_numbers INT)")

	# create 100 random numbers
	list_of_numbers = []

	count = 0

	while count < 100:
		list_of_numbers.append(int(100*random.random()))
		count += 1

	# print list_of_numbers

	list_of_numbers = [(x,) for x in list_of_numbers]

	# print list_of_numbers

	# insert these 100 numbers into database
	c.executemany("INSERT INTO numbers VALUES (?)", list_of_numbers)

	c.execute("SELECT * from numbers ORDER BY random_numbers ASC")
	
	rows = c.fetchall()

	for row in rows:
		print row