from flask_restful import Resource, reqparse
from .services import PurchaseOrderService

class PurchaseOrders(Resource):

    __service__ = PurchaseOrderService()

    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição válida.'
    )
    parser.add_argument(
        'quantity',
        type=int,
        required=True,
        help='Informe uma quantidade válida.'
    )

    def get(self):
        return self.__service__.find_all()
    
    def post(self):
        data = PurchaseOrders.parser.parse_args()
        return self.__service__.create(**data)

class PurchaseOrderById(Resource):

    __service__ = PurchaseOrderService()

    def get(self, id):
        return self.__service__.find_by_id(id)