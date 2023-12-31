from flask_restful import Api
from resources.Root import Root
from resources.auth import ClientRegister, Login, Logout, TokenRefresh
from resources.report import GetProductReport
from resources.user import UserRegister, UsersList, UserDelete, CompanyProducts
from resources.category import CategoryRegister, CategoriesList, CategoryDelete
from resources.product import ProductRegister, ProductsList, ProductDelete, ProductByID, ProductsByCategory

api = Api()

api.add_resource(Root, '/')

#User's APIs as Client (Register, Login, Logout, Refresh)
api.add_resource(ClientRegister,'/client/register')
api.add_resource(Login,'/client/login')
api.add_resource(Logout,'/client/logout')
api.add_resource(TokenRefresh,'/refresh')

#User's APIs as Company still to be add

#Users's APIs (List, Delete)
api.add_resource(UserRegister, '/user/register')
api.add_resource(UsersList, '/users')
api.add_resource(UserDelete, '/user/delete')

#Product's APIs (Add, List, GetProductsByCompany, GetProductByID, Delete)
api.add_resource(ProductRegister, '/product/register')
api.add_resource(ProductsList, '/products')
api.add_resource(CompanyProducts,'/company/products')
api.add_resource(ProductByID, '/products/<string:id>')
api.add_resource(ProductsByCategory,'/products/category')
api.add_resource(ProductDelete, '/product/delete')

#Category's APIs (Add, List, Delete)
api.add_resource(CategoryRegister, '/category/register')
api.add_resource(CategoriesList, '/categories')
api.add_resource(CategoryDelete, '/category/delete')

#Report's APIs (GetProductReport)
api.add_resource(GetProductReport, '/product/report')
