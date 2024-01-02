#!/usr/bin/python3
"""Starts a Flask web application.
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the
    text variable (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value of
    the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Display 'Python by default followed by <text> """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>")
def number(n):
    if n.isdigit():
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
