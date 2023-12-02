from flask_restful import Api
from resources.Root import Root
from resources.user import UserRegister, Users, UserDelete

api = Api()

api.add_resource(Root, '/')

api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/users')
api.add_resource(UserDelete, '/userdelete')
