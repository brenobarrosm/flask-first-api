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

class PurchaseOrdersItems(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Informe um ID'
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição'
    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='Informe um preço'
    )

    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
            
        return jsonify({'message': f'Pedido {id} não encontrado :('})
    
    def post(self, id):
        req_data = PurchaseOrdersItems.parser.parse_args()

        for po in purchase_orders:
            if po['id'] == id:
                item = {
                    'id': req_data['id'],
                    'description': req_data['description'],
                    'price': req_data['price']
                }
                po['items'].append(item)
                return jsonify(po)
        
        return jsonify({'message': f'Pedido {id} não encontrado :('})