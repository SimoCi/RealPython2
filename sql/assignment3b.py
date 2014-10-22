import sqlite3
from sys import exit

with sqlite3.connect("newnum.db") as conn:
	c = conn.cursor()
	result = 0

	while c:
		operation = raw_input("Perform Aggregtion or EXIT program ?> ")

		if operation == 'AVG'.lower():
			# perform aggregation: 'average'
			c.execute("SELECT avg(random_numbers) from numbers")

			result = c.fetchone()

			print "Average = ", result
		elif operation == 'MAX'.lower():
			# perform aggregation: 'average'
			c.execute("SELECT max(random_numbers) from numbers")

			result = c.fetchone()

			print "Maximum = ", result
		elif operation == 'MIN'.lower():
			# perform aggregation: 'average'
			c.execute("SELECT min(random_numbers) from numbers")

			result = c.fetchone()

			print "Minimum = ", result
		elif operation == 'SUM'.lower():
			# perform aggregation: 'average'
			c.execute("SELECT sum(random_numbers) from numbers")

			result = c.fetchone()

			print "Sum = ", result
		elif operation == 'EXIT'.lower():
			print "Exit program."
			exit(0)
		else:
			print "Please perform aggregation (AVG, MAX, MIN, or SUM) or EXIT."

