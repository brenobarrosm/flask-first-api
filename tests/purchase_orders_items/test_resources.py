import json

def test_get_items_by_purchase_order_id(test_client, seed_db):
    response = test_client.get(f'/purchase-orders/{seed_db["purchase_order"].id}/items')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == seed_db['items'].id
    assert response.json[0]['description'] == seed_db['items'].description
    assert response.json[0]['price'] == seed_db['items'].price

def test_get_items_by_purchase_order_id_not_found(test_client):
    id = 909
    response = test_client.get(f'/purchase-orders/{id}/items')

    assert response.status_code == 200
    assert response.json['message'] == 'Informe um ID válido.'

def test_post_purchase_orders_items(test_client, seed_db):
    item = {
        'description': 'Descrição Teste Item 2',
        'price': 574.90
    }

    response = test_client.post(
        f'purchase-orders/{seed_db["purchase_order"].id}/items',
        data=json.dumps(item),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] is not None
    assert response.json['description'] == item['description']
    assert response.json['price'] == item['price']

def test_post_invalid_description(test_client, seed_db):
    item = {
        'price': 574.90
    }

    response = test_client.post(
        f'purchase-orders/{seed_db["purchase_order"].id}/items',
        data=json.dumps(item),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição válida.'

def test_post_invalid_price(test_client, seed_db):
    item = {
        'description': 'Descrição Teste Item 4',
    }

    response = test_client.post(
        f'purchase-orders/{seed_db["purchase_order"].id}/items',
        data=json.dumps(item),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Informe um preço válido.'

def test_post_items_id_not_found(test_client):
    id = 999999

    item = {
        'id': 1,
        'description': 'Item Teste',
        'price': 99.90
    }

    response = test_client.post(
        f'purchase-orders/{id}/items',
        data=json.dumps(item),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['message'] == 'Informe um ID válido.'