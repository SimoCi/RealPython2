# homework - SQL functions

"""Output the car's make and model on one line, the quantity on another line, and then
the order count on the next line. The latter is a bit difficult, but please try it first 
before looking at the solution. Remember: Google-it-first!"""

import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	c.execute("SELECT * FROM inventory""")

	rows = c.fetchall()

	for row in rows:
		print "Make: {0}, Model: {1}".format(row[0], row[1])
		print "Quantity: ", str(row[2]) 

		c.execute("""SELECT count(order_date) 
			FROM orders 
			WHERE make = ? and model = ?""",
			(row[0], row[1]))

		order_count = c.fetchone()[0]

		print "Order Count: ", order_count
		print