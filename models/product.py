from db import db
import uuid

class ProductModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(36), primary_key = True, nullable = False)
    idCompany = db.Column(db.String(36), db.ForeignKey('user.id'), nullable = False)
    category = db.Column(db.String(80), nullable = False)
    name = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String(1024))
    quantity = db.Column(db.Integer)

    def __init__(self, name, idCompany, category, description, quantity):
        self.idCompany = idCompany
        self.category = category
        self.name = name
        self.description = description
        self.quantity = quantity
        self.id = str(uuid.uuid4())

    def json(self):
        return{
            'id': self.id,
            'idCompany': self.idCompany,
            'category': self.category,
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity
        }

    #add product
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #delete product
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    #get product by id
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    #get product by idCompany
    @classmethod
    def find_by_idCompany(cls, _idCompany):
        return cls.query.filter_by(idCompany = _idCompany).first()

    #get all products by idCompany
    @classmethod
    def find_all_by_idCompany(cls, _idCompany):
        return cls.query.filter_by(idCompany = _idCompany).all()

    #get all products by idCategory
    @classmethod
    def find_all_by_category(cls, _category):
        return cls.query.filter_by(category = _category).all()

    #get all products
    @classmethod
    def find_all(cls):
        return cls.query.all()