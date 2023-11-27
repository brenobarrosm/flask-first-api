from flask import Flask, jsonify
from flask_restful import Api, Resource

from purchase_orders.resources import PurchaseOrders

app = Flask(__name__)
api = Api(app)
    
api.add_resource(PurchaseOrders, '/purchase-orders')

app.run(port=5000)