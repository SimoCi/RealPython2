# INSERT command


# import the sqLite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

# commit changes -- commit current transaction
conn.commit()

# close connection to database
conn.close()

# make the above code more compact using the 'with' keyword
# commit the current transaction without using the commit() method
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO populations VALUES('Trst', 'FTT', 200000)")
	c.execute("INSERT INTO populations VALUES('Muja', 'FTT', 8000)")