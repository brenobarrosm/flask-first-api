from flask import jsonify
from flask_restful import Resource, reqparse

purchase_orders = [
    {
        'id': 1,
        'description': 'Descrição do Item 01',
        'items': [
            {
                'id': 1,
                'description': 'Item do Pedido 01',
                'price': 19.90
            }
        ]
    }
]

class PurchaseOrdersItems(Resource):
    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
        return jsonify({'message': 'Informe um ID válido.'})