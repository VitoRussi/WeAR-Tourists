from db import db
from sqlalchemy.sql import text
import uuid

class ReportModel(db.Model):
    __tablename__ = 'report'

    id = db.Column(db.String(36), primary_key=True, nullable = False)
    idProduct = db.Column(db.String(36), db.ForeignKey('product.id'), nullable = False)
    report_path = db.Column(db.Text())
    has_json_report = db.Column(db.Boolean, nullable = False)
    has_model = db.Column(db.Boolean, nullable = False)

    def __init__(self, idProduct, has_json_report, has_model):
        self.id = str(uuid.uuid4())
        self.idProduct = idProduct
        nome_file = "report" + str(id) + ".json"
        self.report_path = "reports/" + nome_file
        self.has_json_report = has_json_report
        self.has_model = has_model

    def json(self):
        return {
            'id': self.id,
            'idProduct': self.idProduct,
            'report_path': self.report_path,
            'has_json_report': self.has_json_report
            }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def get_has_model(self):
        return {
            'model': self.model,
        }

    def get_has_json_report(self):
        return{
            'has_json_report': self.has_json_report
        }