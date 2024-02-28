import json

def test_get_items_by_purchase_order_id(test_client):
    response = test_client.get('/purchase-orders/1/items')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == 1

def test_get_items_by_purchase_order_id_not_found(test_client):
    id = 909
    response = test_client.get(f'/purchase-orders/{id}/items')

    assert response.status_code == 200
    assert response.json['message'] == 'Informe um ID válido.'

def test_post_purchase_orders_items(test_client):
    item = {
        'id': 2,
        'description': 'Descrição Teste Item 2',
        'price': 574.90
    }

    response = test_client.post(
        'purchase-orders/1/items',
        data=json.dumps(item),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] == 2
    assert response.json['price'] == 574.90

def test_post_invalid_id(test_client):
    item = {
        'description': 'Descrição Teste Item 2',
        'price': 574.90
    }

    response = test_client.post(
        'purchase-orders/1/items',
        data=json.dumps(item),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['id'] == 'Informe um ID válido.'

def test_post_invalid_description(test_client):
    item = {
        'id': 3,
        'price': 574.90
    }

    response = test_client.post(
        'purchase-orders/1/items',
        data=json.dumps(item),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição válida.'

def test_post_invalid_price(test_client):
    item = {
        'id': 4,
        'description': 'Descrição Teste Item 4',
    }

    response = test_client.post(
        'purchase-orders/1/items',
        data=json.dumps(item),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Informe um preço válido.'

def test_post_items_id_not_found(test_client):
    id = 999

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