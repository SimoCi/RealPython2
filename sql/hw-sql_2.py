# homework

import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	c.execute("""CREATE table orders 
		(make TEXT, model TEXT, order_date TEXT)""")

	cars = [
	('Ford', 'Fiesta', '2009-11-04'),
	('Ford', 'Fiesta', '2009-11-09'),
	('Ford', 'Fiesta', '2010-01-04'),
	('Ford', 'Focus', '2009-10-14'),
	('Ford', 'Focus', '2009-11-17'),
	('Ford', 'Focus', '2010-01-21'),
	('Ford', 'Ka', '2009-10-31'),
	('Ford', 'Ka', '2009-11-08'),
	('Ford', 'Ka', '2009-11-28'),
	('Honda', 'Pagoor', '2012-01-13'),
	('Honda', 'Pagoor', '2012-04-20'),
	('Honda', 'Pagoor', '2013-09-30'),
	('Honda', 'Gorf', '2013-04-09'),
	('Honda', 'Gorf', '2013-08-21'),
	('Honda', 'Gorf', '2014-10-19')
	]

	c.executemany("INSERT INTO orders VALUES (?,?,?)", cars)

	c.execute("SELECT * FROM orders ORDER BY order_date ASC")

	rows = c.fetchall()

	for row in rows:
	 	print "Make: " row[0]
	 	print "Model: ", row[1]
	 	print "Order Date: ", row[2]
	 	print

