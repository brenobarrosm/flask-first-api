# Settings file

from flask import Flask, jsonify, request

app = Flask(__name__)

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

#GET purchase_orders
@app.route('/purchase-orders')
def get_purchase_orders():
    return jsonify(purchase_orders)

#GET purchese_orders_by_id
@app.route('/purchase-orders/<int:id>')
def get_purchase_orders_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
    return jsonify({'message': f'Pedido {id} não encontrado :('})

#POST puchase_orders
@app.route('/purchase-orders', methods=['POST'])
def create_purchase_order():
    request_data = request.get_json()
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items': []
    }

    purchase_orders.append(purchase_order)

    return jsonify(purchase_order)

#GET purchase_orders_items
@app.route('/purchase-orders/<int:id>/items')
def get_purchase_orders_items(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po['items'])
    return jsonify({'message': f'Pedido {id} não encontrado :('})

#POST purchase_orders_items
@app.route('/purchase-orders/<int:id>/items', methods=['POST'])
def create_purchase_orders_items(id):
    request_data = request.get_json()
    for po in purchase_orders:
        if po['id'] == id:
            item = {
                'id': request_data['id'],
                'description': request_data['description'],
                'price': request_data['price']
            }
            po['items'].append(item)
            return jsonify(po)
    
    return jsonify({'message': f'Pedido {id} não encontrado :('})

@app.route('/')
def home():
    return "Hello World!"

app.run(port=5000)