#!/usr/bin/python3
"""starts a Flask web application"""
from flask import render_template
from models import storage
from flask import Flask
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_cities():
    """display a HTML page: (inside the tag BODY)"""
    result = storage.all("State")
    return render_template('8-cities_by_states.html', states=result)


@app.teardown_appcontext
def teardown_db(self):
    """closes or otherwise deallocates the resource if it exists"""
    storage.close()


if __name__ == '__main__':
    """the code not be executed when imported"""
    app.run(host='0.0.0.0', port=5000)
