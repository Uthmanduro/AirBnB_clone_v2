#!/usr/bin/python3
"""modules that creates a flask app"""
from flask import Flask, render_template
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
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """display "pytonh" followed by value of the text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display "n is a number" if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """displays a html page if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
