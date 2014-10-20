# import from cvs

# import the csv library
import csv

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# open the csv file and assign it to variable 'employees'
	employees = csv.reader(open("employees.csv", "rU"))

	# create new table 'employees'
	c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	# insert data into table 'employees' using the executemany() method
	c.executemany("INSERT INTO employees(firstname, lastname) VALUES (?, ?)", employees)