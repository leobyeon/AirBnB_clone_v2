#!/usr/bin/python3
# starts a Flask web application
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_sesh(param):
    """ close current session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_states():
    """ display an HTML page """
    states = storage.all("State").values()
    cities = storage.all("City").values()
    return render_template(
            '8-cities_by_states.html', states=states, cities=cities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
