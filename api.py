from flask_restful import Api
from resources.Root import Root
from resources.user import UserRegister, UsersList, UserDelete, CompanyProducts
from resources.category import CategoryRegister, CategoriesList, CategoryDelete
from resources.product import ProductRegister, ProductsList, ProductDelete

api = Api()

api.add_resource(Root, '/')

api.add_resource(UserRegister, '/userregister')
api.add_resource(UsersList, '/userslist')
api.add_resource(UserDelete, '/userdelete')
api.add_resource(ProductRegister, '/productregister')
api.add_resource(ProductsList, '/productslist')
api.add_resource(ProductDelete, '/productdelete')
api.add_resource(CategoryRegister, '/categoryregister')
api.add_resource(CategoriesList, '/categorieslist')
api.add_resource(CategoryDelete, '/categorydelete')
api.add_resource(CompanyProducts,'/companyproducts')