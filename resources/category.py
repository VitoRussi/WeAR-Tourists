from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request

from models.category import CategoryModel
from models.product import ProductModel


class CategoryRegister(Resource):
    # API POST class Categoria
    @jwt_required()
    def post(self):
        args = request.json
        categoria = CategoryModel(**args)
        categoria.save_to_db()
        return 200

class CategoriesList(Resource):
    #API GET class Categoria
    @jwt_required()
    def get(self):
        categorie = CategoryModel.find_all()
        print(categorie)
        categoria_json = [c.json() for c in categorie]
        return categoria_json, 200

class CategoryDelete(Resource):
    #API DELETE class Categoria
    @jwt_required()
    def delete(self):
        args = request.json
        categoria = CategoryModel.find_by_name(args["name"])
        if categoria:
            if len(ProductModel.find_all_by_category(categoria.name)) > 0:
                return "Category not deleatable, Category has products in it", 403
            categoria.delete_from_db()
            return "Category deleted", 200
        return "Category does not exists", 404