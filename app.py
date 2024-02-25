from flask import Flask
from flask_restful import Api

from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems

app = Flask(__name__)
api = Api(app)
    
api.add_resource(PurchaseOrders, '/purchase-orders')
api.add_resource(PurchaseOrdersById, '/purchase-orders/<int:id>')
api.add_resource(PurchaseOrdersItems, '/purchase-orders/<int:id>/items')

app.run(port=5000)