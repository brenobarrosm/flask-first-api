import pytest
from db import db

from purchase_orders.model import PurchaseOrdersModel
from purchase_orders_items.model import PurchaseOrdersItemsModel

@pytest.fixture()
def seed_db():
    po = PurchaseOrdersModel('Pedido de testes')
    db.session.add(po)
    db.session.commit()

    poi = PurchaseOrdersItemsModel('Item 1', 19.90, po.id)
    db.session.add(poi)
    db.session.commit()

    yield {'purchase_order': po, 'items': poi}

@pytest.fixture(scope='function', autouse=True)
def clear_db():
    db.session.query(PurchaseOrdersItemsModel).delete()
    db.session.query(PurchaseOrdersModel).delete()
    db.session.commit()


