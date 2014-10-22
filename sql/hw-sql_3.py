# homework - SQL functions

"""Using the COUNT() function, calculate the total number of orders for each make and model."""

import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	sql_total_orders = {
	# 'Ford': "SELECT count(make) FROM orders WHERE make = 'Ford'",
	'Fiesta count': "SELECT count(make) FROM orders WHERE model = 'Fiesta'",
	'Focus count': "SELECT count(make) FROM orders WHERE model = 'Focus'",
	'Ka count': "SELECT count(make) FROM orders WHERE model = 'Ka'",
	# 'Honda': "SELECT count(order_date) FROM orders WHERE make = 'Honda'",
	'Pagoor': "SELECT count(make) FROM orders WHERE model = 'Pagoor'",
	'Gorf': "SELECT count(make) FROM orders WHERE model = 'Gorf'"
	}

	# c.execute("SELECT count(order_date) FROM orders WHERE make = 'Ford' and model = 'Fiesta'")

	for key, value in sql_total_orders.iteritems():

		c.execute(value)

		result = c.fetchone()

		print key + ": ", result[0]