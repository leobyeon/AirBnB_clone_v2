#!/usr/bin/python3
# starts a Flask web application
from flask import Flask
from flask import render_template
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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text="is cool"):
    """ returns text """
    copy = str(text).replace('_', ' ')
    return "Python %s" % copy


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ returns 'n is a number' only if n is an integer """
    return "n is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ returns 'n is a number' only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
