from db import db
import uuid

class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.String(36), primary_key = True, nullable = False)
    name = db.Column(db.String(80), primary_key = True, nullable = False)

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name

    def json(self):
        return{
            'id': self.id,
            'name': self.name
        }

    #save category
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #get category
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    #get category by id
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    #get category by name
    @classmethod
    def find_by_name(cls, _name):
        return cls.query.filter_by(name = _name).first()

    #get all categories
    @classmethod
    def find_all(cls):
        return cls.query.all()
