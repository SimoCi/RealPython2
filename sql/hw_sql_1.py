import sqlite3

with sqlite3.connect("cars.db") as conn:
	
	cursor = conn.cursor()

	cars = [
	('Ford', 'Fiesta', 12), 
	('Ford', 'Focus', 7),
	('Ford', 'Ka', 21), 
	('Honda', 'Pagoor', 11), 
	('Honda', 'Gorf', 4)
	]

	print "\nInsert Data...\n"

	cursor.executemany("INSERT into inventory values (?, ?, ?)", cars)

	cursor.execute("SELECT * from inventory")

	rows = cursor.fetchall()

	for row in rows:
		print "Make '{0}', Model '{1}', Quantity '{2}'".format(row[0], row[1], row[2])

	print "\nUpdate 2 records of your choice\n"

	cursor.execute("UPDATE inventory SET quantity = 11 where model = 'Fiesta'")
	cursor.execute("UPDATE inventory SET quantity = 10 where model = 'Pagoor'")

	cursor.execute("SELECT * from inventory")

	rows = cursor.fetchall()

	for row in rows:
		print "Make '{0}', Model '{1}', Quantity '{2}'".format(row[0], row[1], row[2])

	print "\nPrinting only Ford models\n"

	for row in rows:
		if row[0] == "Ford":
			print "Make '{0}', Model '{1}', Quantity '{2}'".format(row[0], row[1], row[2])
