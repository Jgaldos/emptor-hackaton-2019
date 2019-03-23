# app.py
from flask import Flask
from flask_restful import Resource, Api, reqparse

import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('profile')
parser.add_argument('name')
parser.add_argument('address')
parser.add_argument('id')
parser.add_argument('phone')
parser.add_argument('email')


class Score(Resource):
    def post(self):

        args = parser.parse_args()

        profile_json = args['profile']

        profile_data = json.loads(profile_json)

        id_data = id_score(profile_data['id'])
        name_data = name_score(profile_data['name'])
        address_data = address_score(profile_data['address'])
        email_data = email_score(profile_data['email'])
        phone_data = phone_score(profile_data['phone'])

        details = {
            'id': id_data['details'],
            'name': name_data['details'],
            'address': address_data['details'],
            'email': email_data['details'],
            'phone': phone_data['details'],
        }

        return {'id': id_data['score'],
                'name': name_data['score'],
                'address': address_data['score'],
                'email': email_data['score'],
                'phone': phone_data['score'],
                'details': details}, 201


def address_score(address):
    return {'score': 100,
            'details': {
                'gmaps': False
            }}


def id_score(id):
    return {'score': 100,
            'details': {
                'sunat': True
            }}


def email_score(email):
    return {'score': 100,
            'details': {
                'checklist': True
            }}


def phone_score(phone):
    return {'score': 100,
            'details': {
                'textmagic': True
            }}


def name_score(name):
    return {'score': 100,
            'details': {
                'sunat': True,
                'name': name,
                'cip': True,
            }}


api.add_resource(Score, '/peru')

if __name__ == '__main__':
    app.run(debug=True)
