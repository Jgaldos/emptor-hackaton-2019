from flask_restful import Resource, Api, reqparse

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

        return self.evaluate(args)

    def evaluate(self, profile_json):

        profile_data = profile_json

        profile_id = profile_data['identification']
        profile_name = profile_data['name']
        profile_address = profile_data['address']['address']
        profile_phone = profile_data['phone']['area_code'] + profile_data['phone']['number']
        profile_email = profile_data['email']

        id_data = id_score(profile_id)
        name_data = name_score(profile_name)
        address_data = address_score(profile_address)
        email_data = email_score(profile_email)
        phone_data = phone_score(profile_phone)

        details = {
            'id': id_data['details'],
            'name': name_data['details'],
            'address': address_data['details'],
            'email': email_data['details'],
            'phone': phone_data['details'],
        }

        total_score = (id_data['score'] + name_data['score'] + address_data['score'] + email_data['score'] + phone_data['score']) / 5

        return {
            "profile": {
                "Id_document": profile_id,
                "Name": profile_name,
                "Address": profile_address,
                "Phone": profile_phone,
                "Email": profile_email,
            },
            "score": {
                'id': id_data['score'],
                'name': name_data['score'],
                'address': address_data['score'],
                'email': email_data['score'],
                'phone': phone_data['score'],
                'details': details
            },
            # "total_score": sum(total_score_lst) / len(total_score_lst),
            "total_score": total_score,

        }, 201



def address_score(address):
    return {'score': 0,
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
                'osiptel': True
            }}


def name_score(name):
    return {'score': 100,
            'details': {
                'sunat': True,
                'name': name,
                'cip': True,
            }}

