
from flask_restful import Resource


mock_results = {
    '1': {
        'name': 'Jose Galdos',
        "address": {
            "state": "LM-O",
            "city": "Lima",
            "address": "Avenida Comandante, 390",
            "zip_code": "1414"
        },
        "phone": {
            "area_code": "01",
            "number": "0681-5294",
            "extension": "",
          },
        "identification": {
            "type": "DNI",
            "number": "843641869"
          },
        "email": "jose_galdos@gmail.com",
    },
    '2': {
        'name': 'Pedro Munoz',
        "address": {
            "state": "AQ-C",
            "city": "Arequipa",
            "address": "Campina paisajista 666",
            "zip_code": "1414"
        },
        "phone": {
            "area_code": "054",
            "number": "123-4566",
            "extension": "",
        },
        "identification": {
            "type": "DNI",
            "number": "1287004"
        },
        "email": "pedro@nofake.com",
    },
    '3': {
        'name': 'Roger Peralta',
        "address": {
            "state": "CU",
            "city": "Cusco",
            "address": "Urb. Los Sauces c-1",
            "zip_code": "1414"
        },
        "phone": {
            "area_code": "084",
            "number": "984789867",
            "extension": "",
        },
        "identification": {
            "type": "DNI",
            "number": "1111111"
        },
        "email": "roger4@testuser.com",
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


