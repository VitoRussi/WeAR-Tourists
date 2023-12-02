from flask_restful import Resource
from flask import request

from models.user import UserModel


class UserRegister(Resource):

    def post(self):
        args = request.json
        #print(args["Nome"])
        utente = UserModel(**args)
        utente.save_to_db()
        return 200

class Users(Resource):

    def get(self):
        utenti = UserModel.find_all()
        print(utenti)
        utenti_json = [u.json(u) for u in utenti]
        return utenti_json, 200

class UserDelete(Resource):
    def delete(self):
        args = request.json
        utente = UserModel.find_by_id(args["id"])
        if utente:
            utente.delete_from_db()
            return "User deleted", 200
        return "User doesn't exists", 404