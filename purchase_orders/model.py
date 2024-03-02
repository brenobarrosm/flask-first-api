from db import db

class PurchaseOrdersModel(db.Model):
    __tablename__ = 'purchase_order'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, description):
        self.description = description

    # Iterates over the columns of a table to create a dict
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod #The first argument of the function will be the instance of the class
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()