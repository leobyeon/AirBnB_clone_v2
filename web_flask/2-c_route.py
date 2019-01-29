#!/usr/bin/python3
# starts a Flask web application
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns a string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns a string """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ returns text """
    copy = str(text).replace('_', ' ')
    return "C %s" % copy


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
