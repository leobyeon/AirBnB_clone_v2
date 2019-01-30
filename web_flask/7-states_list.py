#!/usr/bin/python3
# starts a Flask web application
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_sesh(param):
    """ close current session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """ display an HTML page """
    states = []
    state_data = storage.all("State")
    for key, val in state_data.items():
        states.append(val)
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
