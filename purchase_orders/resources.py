from flask import jsonify
from flask_restful import Resource

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

class PurchaseOrders(Resource):

    def get(self):
        return jsonify(purchase_orders)