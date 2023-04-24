#!/usr/bin/python3
"""displays a list of state"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """displays a list of all state objects in the db"""
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(exception):
    """it removes the current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
