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

    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Informe um ID válido.'
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição válida.'
    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='Informe um preço válido.'
    )

    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
        return jsonify({'message': 'Informe um ID válido.'})
    
    def post(self, id):

        args = PurchaseOrdersItems().parser.parse_args()

        item = {
            'id': args['id'],
            'description': args['description'],
            'price': args['price']
        }

        for po in purchase_orders:
            if po['id'] == id:
                po['items'].append(item)
                return jsonify(item)
            
        return jsonify({'message': 'Informe um ID válido.'})