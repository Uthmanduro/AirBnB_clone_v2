#!/usr/bin/python3
"""modules that creates a flask app"""
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
	"""displays the homepage"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_func():
	"""displays hbnb"""
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
	"""display "C" followed by the variable passed as argument"""
	return f"C {text.replace('_', ' ')}"

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
	"""display "pytonh" followed by value of the text"""
	return f"Python {text.replace('_', ' ')}"

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
	"""display "n ins a number" if n is an integer"""
	return f"{n} is a number"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
