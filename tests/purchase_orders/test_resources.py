import json

def test_get_purchase_orders(test_client):
    response = test_client.get('/purchase-orders')

    assert response.status_code == 200
    assert response.json[0]['id'] == 1

def test_post_purchase_orders(test_client):
    obj = {
        'id': 2,
        'description': 'Purchase Order ID 2'
    }

    response = test_client.post(
        '/purchase-orders',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] == obj['id']
    assert response.json['description'] == obj['description']
    assert response.json['items'] == []