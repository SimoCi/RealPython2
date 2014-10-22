# homework

import sqlite3

with sqlite3.connect("cars.db") as conn:

	c = conn.cursor()

	c.execute("SELECT inventory.Make, inventory.Model, inventory.quantity, orders.order_date\
		FROM inventory, orders WHERE inventory.Model = orders.model ORDER BY\
		orders.order_date ASC")

	rows = c.fetchall()

	for row in rows:
		print "Make: {0}, Model: {1}".format(row[0], row[1])
		print "Quantity: ", str(row[2]) 
		print "Order Date: ", row[3]
		print