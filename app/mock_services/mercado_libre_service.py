
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
            "number": "0681-52947",
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
            "state": "LO-C",
            "city": "Loreto",
            "address": "Test Address 123",
            "zip_code": "1414"
        },
        "phone": {
            "area_code": "05",
            "number": "9835-86953",
            "extension": "",
        },
        "identification": {
            "type": "DNI",
            "number": "75980754"
        },
        "email": "mupetest@fastmail.com",
    },
    '3': {
        'name': 'Roger Peralta',
        "address": {
            "state": "AR-J",
            "city": "Arequipa",
            "address": "Calle America 827",
            "zip_code": "960"
        },
        "phone": {
            "area_code": "54",
            "number": "9654-43078",
            "extension": "",
        },
        "identification": {
            "type": "DNI",
            "number": "64905312"
        },
        "email": "eddie.pa@company.com",
    },
    '4': {
        'name': 'Victoria Melo',
        "address": {
            "state": "CZ-B",
            "city": "Cuzco",
            "address": "Aranwa Spa",
            "zip_code": "487"
        },
        "phone": {
            "area_code": "03",
            "number": "9430-65187",
            "extension": "",
        },
        "identification": {
            "type": "DNI",
            "number": "654879056"
        },
        "email": "Vick@hotmail.com",
    },
}


class MockMercadoLibre(Resource):
    def get(self, user_id):
        return mock_results[user_id]


