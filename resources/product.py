from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request

from models.product import ProductModel
from models.report import ReportModel
from models.user import UserModel
from models.category import CategoryModel

class ProductRegister(Resource):
    #API POST class Prodotto
    @jwt_required()
    def post(self):
        args = request.json
        prodotto = ProductModel(args["name"], args["idCompany"], args["category"], args["description"], args["quantity"])
        report = ReportModel(prodotto.id, args["has_json_report"], args["has_model"])
        if UserModel.find_by_id(prodotto.idCompany):
            if CategoryModel.find_by_name(prodotto.category):
                prodotto.save_to_db()
                report.save_to_db()
                return "Prodotto salvato", 200
            categoria = CategoryModel(prodotto.category)
            categoria.save_to_db()
            prodotto.save_to_db()
            report.save_to_db()
            return "Categoria non esistente. Categoria creata, prodotto registrato", 200
        return "Azienda non esistente", 404

class ProductsList(Resource):
    #API GET class Prodotto for all products
    @jwt_required()
    def get(self):
        prodotti = ProductModel.find_all()
        print(prodotti)
        prodotti_json = [p.json() for p in prodotti]
        return prodotti_json, 200

class ProductByID(Resource):
    #API GET class Prodotto given id
    @jwt_required()
    def get(self):
        args = request.json
        prodotto = ProductModel.find_by_id(args["id"])
        if prodotto:
            return prodotto.json(), 200
        return "Prodotto non trovato", 404

class ProductsByCategory(Resource):
    #API GET class Prodotto for products given their Category
    @jwt_required()
    def get(self):
        args = request.json
        prodotti = ProductModel.find_all_by_category(args["category"])
        print(prodotti)
        prodotti_json = [p.json() for p in prodotti]
        return prodotti_json, 200

class ProductDelete(Resource):
    #API DELETE class Prodotto
    @jwt_required()
    def delete(self):
        args = request.json
        prodotto = ProductModel.find_by_id(args["id"])
        if prodotto:
            prodotto.delete_from_db()
            return "Product deleted", 200
        return "Product does not exist", 404