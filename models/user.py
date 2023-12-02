from db import db
from sqlalchemy.sql import text
import uuid

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(320), nullable=False)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))

    roles = ["client", "company"]

    def __init__(self, password, role, firstname, lastname, email):
        self.password = password
        self.role = role
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.id = str(uuid.uuid4())

    def json(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'role': self.role,
        }

    @classmethod
    def json_from_list(cls, args):
        return {
            'id': args[0],
            'firstname': args[4],
            'lastname': args[5],
            'email': args[3],
            'role': args[2]
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def edit_param(self, params):
        try:
            for couple in params:
                for key in couple:
                    value = couple[key]

                    self.query.filter_by(id=self.id).update({key: value})

        except Exception as e:
            print("Exception:", e)
        db.session.commit()

    def verify_password(self, password):
        return password == self.password

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_email(cls, _email):
        return cls.query.filter_by(email=_email).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def query_example(cls):
        query = "SELECT * FROM mydb.user"
        return db.session.execute(text(query)).all()

