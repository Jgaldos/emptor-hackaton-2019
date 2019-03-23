
from flask_restful import Resource


mock_results = {
    '1': {
        'name': 'Jose galdos',
        "address": {
            "state": "AR-C",
            "city": "Palermo",
            "address": "Test Address 123",
            "zip_code": "1414"
        },
        "phone": {
            "area_code": "01",
            "number": "1111-1111",
            "extension": "",
          },
        "identification": {
            "type": "DNI",
            "number": "1111111"
          },
        "email": "test_user_38730994@testuser.com",
    },
    '2': {
        'name': 'Pedro Munoz',
        "address": {
            "state": "AR-C",
            "city": "Palermo",
            "address": "Test Address 123",
            "zip_code": "1414"
        },
        "phone": {
            "area_code": "01",
            "number": "1111-1111",
            "extension": "",
        },
        "identification": {
            "type": "DNI",
            "number": "1111111"
        },
        "email": "test_user_38730994@testuser.com",
    },
    '3': {
        'name': 'Roger Peralta',
        "address": {
            "state": "AR-C",
            "city": "Palermo",
            "address": "Test Address 123",
            "zip_code": "1414"
        },
        "phone": {
            "area_code": "01",
            "number": "1111-1111",
            "extension": "",
        },
        "identification": {
            "type": "DNI",
            "number": "1111111"
        },
        "email": "test_user_38730994@testuser.com",
    },
    '4': {
        'name': 'Victoria Melo',
        "address": {
            "state": "AR-C",
            "city": "Palermo",
            "address": "Test Address 123",
            "zip_code": "1414"
        },
        "phone": {
            "area_code": "01",
            "number": "1111-1111",
            "extension": "",
        },
        "identification": {
            "type": "DNI",
            "number": "1111111"
        },
        "email": "test_user_38730994@testuser.com",
    },
}


class MockMercadoLibre(Resource):
    def get(self, user_id):
        return mock_results[user_id]


