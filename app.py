from flask import Flask, jsonify

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de Compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 49.90
            }
        ]
    }

]

# GET purchase_orders
# GET purchase_orders_by_id
# POST purchase_orders
# GET purchase_orders_items
# POST purchase_orders_items

@app.route('/')
def home():
    return "Hello World"

@app.route('/purchase-orders')
def get_purchase_orders():
    return jsonify(purchase_orders)

@app.route('/purchase-orders/<int:id>')
def get_purchase_orders_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
        else:
            return jsonify({'message': f'Pedido {id} não encontrado'})

app.run(port=5000)