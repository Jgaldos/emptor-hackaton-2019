# app.py
from flask import Flask
from flask_restful import Resource, Api, reqparse

from app.pe.test import test_peru
from app.services.score import Score

app = Flask(__name__)
api = Api(app)

"""
@app.route('/peru')
def Start():
    score = Score()
    return score.get()
"""

api.add_resource(Score, '/peru')


if __name__ == '__main__':
    app.run(host='0.0.0.0')