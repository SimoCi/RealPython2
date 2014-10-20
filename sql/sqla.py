# Create a SQLite3 database and table

# import the sqlite3 library to communicate with SQLite.
import sqlite3

# from the sqlite3 library get the connect function with argument "new.db"
# and assign it to variable conn
# -> created connection object 'conn' to connect to exisring database 'new.db'
# if db doesn't exist, create it.
conn = sqlite3.connect("new.db")

# from the conn object get the cursor function and assign output to variable 'cursor'
# the 'cursor' object is used to execute SQL commands or command with data within db
cursor = conn.cursor()

# from cursor get the function execute that takes a query as a parameter
# creating tble 'population'
cursor.execute("""CREATE TABLE populations
	(city TEXT, state TEXT, population INT)
	""")

# close the database connection
conn.close()