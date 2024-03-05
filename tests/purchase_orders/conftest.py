import pytest
from db import db

from purchase_orders.model import PurchaseOrdersModel

@pytest.fixture()
def seed_db():
    po = PurchaseOrdersModel('Purchase Order Test')
    db.session.add(po)
    db.session.commit()

    yield po

@pytest.fixture(scope='function', autouse=True)
def clear_db():
    db.session.query(PurchaseOrdersModel).delete()
    db.session.commit()