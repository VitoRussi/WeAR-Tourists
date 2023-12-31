import json
from flask_restful import Resource
from flask import request

from models.report import ReportModel

class ReportRegister(Resource):
    def post(self):
        args = request.json
        report = ReportModel(**args)
        report.save_to_db()
        return 200

class ReportList(Resource):
    #API GET class Categoria
    def get(self):
        report = ReportModel.find_all()
        print(report)
        report_json = [r.json() for r in report]
        return report_json, 200

class GetProductReport(Resource):
    def get(self):
        args = request.json

        report = ReportModel.find_by_id_product(args['idProduct'])

        #read report json from file report_path
        with open(report.report_path, 'r') as f:
            report_json = json.load(f)
            if report_json:
                return report_json, 200
            return {'message': 'Report not found'}, 404