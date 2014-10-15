# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask

# create the application object
# create an instance of the Flask class and assign it to variable 'app'
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

# start the development server using the run() method
# app is run when app.py is executed, not when imported by different module
if __name__ == "__main__":
	app.run()