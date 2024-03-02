from flask import jsonify
from flask_restful import Resource, reqparse

from .model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrdersModel

class PurchaseOrdersItems(Resource):

    parser = reqparse.RequestParser()
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
        purchase_order_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(id)

        return [i.as_dict() for i in purchase_order_items]
    
    def post(self, id):

        purchase_order = PurchaseOrdersModel.find_by_id(id)
        
        if purchase_order:
            args = PurchaseOrdersItems().parser.parse_args()
            args['purchase_order_id'] = id

            purchase_orders_item = PurchaseOrdersItemsModel(**args)
            purchase_orders_item.save()

            return purchase_orders_item.as_dict()
     
        return jsonify({'message': 'Informe um ID válido.'})