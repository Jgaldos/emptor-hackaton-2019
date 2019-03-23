# app.py
from flask import Flask
from flask_restful import Resource, Api, reqparse

from app.pe.test import test_peru
from app.services.score import Score
from app.mock_services.mercado_libre_service import MockMercadoLibre

app = Flask(__name__)
api = Api(app)

api.add_resource(Score, '/peru')
api.add_resource(MockMercadoLibre, '/mock_ml/<string:user_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')