from flask import jsonify
from flask_restful import Resource, reqparse

from .model import PurchaseOrdersModel

class PurchaseOrders(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição válida.'
    )

    def get(self):
        purchase_orders = PurchaseOrdersModel.find_all()
        return [po.as_dict() for po in purchase_orders]
    
    def post(self):
        data = PurchaseOrders.parser.parse_args()

        purchase_order = PurchaseOrdersModel(**data)
        purchase_order.save()

        return purchase_order.as_dict()
    
class PurchaseOrderById(Resource):

    def get(self, id):
        purchase_order = PurchaseOrdersModel.find_by_id(id)
        if purchase_order:
            return purchase_order.as_dict()
        return jsonify({'message': 'Informe um ID válido.'})