from flask import jsonify
from flask_restful import Resource, reqparse

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

    parser = reqparse.RequestParser()

    parser.add_argument(
        'id',
        type=int,
        required=True,
        help="Informe um ID"
    )

    parser.add_argument(
        'description',
        type=str,
        required=True,
        help="Informe uma descrição"
    )

    def get(self):
        return jsonify(purchase_orders)
    
    def post(self):
        req_data = PurchaseOrders().parser.parse_args()

        po = {
            'id': req_data['id'],
            'description': req_data['description'],
            'items': []
        }

        purchase_orders.append(po)

        return po
    
class PurchaseOrdersById(Resource):
    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po)
            
        return jsonify({'message': f'Pedido {id} não encontrado :('})