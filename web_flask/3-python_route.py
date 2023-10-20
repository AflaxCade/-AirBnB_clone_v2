#!/usr/bin/python3
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Returns a given string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    """display C followed by the value of the text variable"""
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    """display Python followed by the value of the text variable"""
    return f'Python {text}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None) 
