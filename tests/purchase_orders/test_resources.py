import json

def test_get_purchase_orders(test_client, seed_db):
    response = test_client.get('/purchase-orders')

    assert response.status_code == 200
    assert response.json[0]['id'] == seed_db.id
    assert response.json[0]['description'] == seed_db.description

def test_post_purchase_orders(test_client):
    obj = {'description': 'Purchase Order ID 2'}

    response = test_client.post(
        '/purchase-orders',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] is not None
    assert response.json['description'] == obj['description']

def test_post_empty_description(test_client):
    response = test_client.post(
        '/purchase-orders',
        data=json.dumps({}),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição válida.'

def test_get_purchase_order_by_id(test_client, seed_db):
    response = test_client.get(f'/purchase-orders/{seed_db.id}')

    assert response.status_code == 200
    assert response.json['id'] == seed_db.id
    assert response.json['description'] == seed_db.description

def test_get_purchase_order_not_found(test_client):
    id = 111
    response = test_client.get(f'/purchase-orders/{id}')

    assert response.status_code == 200