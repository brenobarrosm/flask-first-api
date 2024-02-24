from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

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
    
api.add_resource(PurchaseOrders, '/purchase-orders')

app.run(port=5000)