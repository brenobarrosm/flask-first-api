from flask import Flask
from flask_restful import Api
from db import db

from purchase_orders.resources import PurchaseOrders, PurchaseOrderById
from purchase_orders_items.resources import PurchaseOrdersItems

def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/flask-restful'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api.add_resource(PurchaseOrders, '/purchase-orders')
    api.add_resource(PurchaseOrderById, '/purchase-orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase-orders/<int:id>/items')

    # with app.app_context():
    #     db.create_all()

    return app