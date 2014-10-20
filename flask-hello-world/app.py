# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask

# create the application object
# create an instance of the Flask class and assign it to variable 'app'
app = Flask(__name__)


app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

# define a dynamic route
#@app.route("/test")
@app.route("/test/<search_query>")
#def search():
def search(search_query):
#	return "Hello!"
	return "Say %s !" % search_query

# flask converters
# avoid converting any query into a string regardless of the parameter
# convert <value> into an integer
@app.route("/integer/<int:value>")
def int_type(value):
	print "Integer %d" % (value + 1)
	return "Correct"

@app.route("/float/<float:value>")
def float_type(value):
	print "Float %f" % (value + 1)
	return "Correct"

# a dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print "Path %s" % value
	return "Correct"

@app.route("/name/<name>")
def index(name):
	# return "Name %s" % name
	if name.lower() == "simo":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404 

# start the development server using the run() method
# app is ran when app.py is executed, not when ran from a different module
if __name__ == "__main__":
	app.run()