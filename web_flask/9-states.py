#!/usr/bin/python3
# starts a Flask web application
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_sesh(param):
    """ close current session """
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def display_states(id=None):
    """ display an HTML page if no parameter """
    states = storage.all("State").values()
    if id:
        state = None
        for v in states:
            if v.id == id:
                state = v
        return render_template('9-states.html', state=state)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
