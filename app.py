# Settings file

from flask import Flask, jsonify

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
#GET purchase_orders_items
#POST purchase_orders_items

@app.route('/')
def home():
    return "Hello World!"

app.run(port=5000)