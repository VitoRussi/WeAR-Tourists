from flask_restful import Resource
from flask import request

from models.product import ProductModel
from models.user import UserModel
from models.category import CategoryModel

class ProductRegister(Resource):
    #API POST class Prodotto
    def post(self):
        args = request.json
        prodotto = ProductModel(**args)
        if UserModel.find_by_id(prodotto.idCompany):
            if CategoryModel.find_by_name(prodotto.category):
                prodotto.save_to_db()
                return "Prodotto salvato", 200
            categoria = CategoryModel(prodotto.category)
            categoria.save_to_db()
            prodotto.save_to_db()
            return "Categoria non esistente. Categoria creata, prodotto registrato", 200
        return "Azienda non esistente", 404

class ProductsList(Resource):
    #API GET class Prodotto
    def get(self):
        prodotti = ProductModel.find_all()
        print(prodotti)
        prodotti_json = [p.json() for p in prodotti]
        return prodotti_json, 200

class ProductDelete(Resource):
    #API DELETE class Prodotto
    def delete(self):
        args = request.json
        prodotto = ProductModel.find_by_id(args["id"])
        if prodotto:
            prodotto.delete_from_db()
            return "Product deleted", 200
        return "Product does not exist", 404