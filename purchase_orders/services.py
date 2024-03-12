from flask import jsonify
from .model import PurchaseOrdersModel

class PurchaseOrderService:

    def find_all(self):
        purchase_orders = PurchaseOrdersModel.find_all()
        return [po.as_dict() for po in purchase_orders]
    
    def create(self, **kwargs):
        purchase_order = PurchaseOrdersModel(**kwargs)
        purchase_order.save()

        return purchase_order.as_dict() 
    
    def find_by_id(self, id):
        purchase_order = PurchaseOrdersModel.find_by_id(id)
        if purchase_order:
            return purchase_order.as_dict()
        return jsonify({'message': 'Informe um ID válido.'})