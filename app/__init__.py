# app.py
from flask import Flask
from flask_restful import Resource, Api, reqparse

import requests

from app.pe .test import test_peru
from app.services .score import Score
from app.mock_services .mercado_libre_service import MockMercadoLibre
from app.models import db, Verified_ids

app = Flask(__name__)
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:@db:5432/hackaton'
db.init_app(app)


class Verify(Resource):
    def get(self, ml_id):
        user = Verified_ids.query.filter_by(id=ml_id).first()
        if user:
            return user.data()
        else:
            req_ml = MockMercadoLibre()
            response = req_ml.get(str(ml_id))
            score_function = Score()
            if response:
                return score_function.evaluate(response)
            else:
                return {'status': 'not found'}


api.add_resource(Verify, '/peru/<int:ml_id>')
api.add_resource(MockMercadoLibre, '/mock_ml/<string:user_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')