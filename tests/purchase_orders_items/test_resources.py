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