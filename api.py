from flask_restful import Api
from resources.Root import Root
from resources.user import UserRegister, UsersList, UserDelete, CompanyProducts
from resources.category import CategoryRegister, CategoriesList, CategoryDelete
from resources.product import ProductRegister, ProductsList, ProductDelete

api = Api()

api.add_resource(Root, '/')

api.add_resource(UserRegister, '/user/register')
api.add_resource(UsersList, '/users')
api.add_resource(UserDelete, '/user/delete')
api.add_resource(ProductRegister, '/product/register')
api.add_resource(ProductsList, '/products')
api.add_resource(ProductDelete, '/product/delete')
api.add_resource(CategoryRegister, '/category/register')
api.add_resource(CategoriesList, '/categories')
api.add_resource(CategoryDelete, '/category/delete')
api.add_resource(CompanyProducts,'/company/products')