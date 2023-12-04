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
    def get(self):
        utenti = UserModel.find_all()
        print(utenti)
        utenti_json = [u.json() for u in utenti]
        return utenti_json, 200

class UserDelete(Resource):

    #API DELETE class Utente
    def delete(self):
        args = request.json
        utente = UserModel.find_by_id(args["id"])
        if utente:
            utente.delete_from_db()
            return "User deleted", 200
        return "User does not exists", 404

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

class CategoryRegister(Resource):

    # API POST class Categoria
    def post(self):
        args = request.json
        categoria = CategoryModel(**args)
        categoria.save_to_db()
        return 200

class CategoriesList(Resource):
    #API GET class Categoria
    def get(self):
        categorie = CategoryModel.find_all()
        print(categorie)
        categoria_json = [c.json() for c in categorie]
        return categoria_json, 200

class CategoryDelete(Resource):

    #API DELETE class Categoria
    def delete(self):
        args = request.json
        categoria = CategoryModel.find_by_name(args["name"])
        if categoria:
            categoria.delete_from_db()
            return "Category deleted", 200
        return "Category does not exists", 404

class CompanyProducts(Resource):
    #API GET class Prodotto for all
    def get(self):
        args = request.json
        prodottiCompany = ProductModel.find_all_by_idCompany(args["idCompany"])
        print(prodottiCompany)
        prodotti_json = [p.json() for p in prodottiCompany]
        return prodotti_json, 200