from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request

from models.category import CategoryModel
from models.user import UserModel
from models.product import ProductModel

class UserRegister(Resource):
    #API POST class Utente
    def post(self):
        args = request.json
        utente = UserModel(**args)
        utente.save_to_db()
        return 200

class UsersList(Resource):
    #API GET class Utente
    @jwt_required()
    def get(self):
        utenti = UserModel.find_all()
        print(utenti)
        utenti_json = [u.json() for u in utenti]
        return utenti_json, 200

class UserDelete(Resource):
    #API DELETE class Utente
    @jwt_required()
    def delete(self):
        args = request.json
        utente = UserModel.find_by_id(args["id"])
        if utente:
            utente.delete_from_db()
            return "User deleted", 200
        return "User does not exists", 404

class CompanyProducts(Resource):
    #API GET class Prodotto for all
    @jwt_required()
    def get(self):
        args = request.json
        prodottiCompany = ProductModel.find_all_by_idCompany(args["idCompany"])
        print(prodottiCompany)
        prodotti_json = [p.json() for p in prodottiCompany]
        return prodotti_json, 200

class CategoryProducts(Resource):
    #API GET class Prodotto for all
    @jwt_required()
    def get(self):
        args = request.json
        prodottiCategory = ProductModel.find_all_by_idCompany(args["idCompany"])
        print(prodottiCompany)
        prodotti_json = [p.json() for p in prodottiCompany]
        return prodotti_json, 200