# app.py
from flask import abort, Flask, jsonify, make_response
from flask_restful import Resource, Api, reqparse

from app.pe.test import get_persons, get_score
from app.services .score import Score

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/')
def index():
    return 'Index Page'

@app.route('/peru/persons', methods=['GET'])
def get_tasks():
    return get_persons()

@app.route('/peru/person/<int:task_id>', methods=['GET'])
def get_peru_score(task_id):
    return get_score(task_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0')