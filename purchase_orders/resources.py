from flask import jsonify
from flask_restful import Resource

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de Compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item 1 do Pedido 1',
                'price': 22.90
            }
        ]
    }
]

class PurchaseOrders(Resource):
    def get(self):
        return jsonify(purchase_orders)