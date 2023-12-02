from flask import Flask
from db import db
from flask_cors import CORS
from api import api

import pymysql

pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

cors = CORS()

def create_app():
    app = Flask(__name__)
    
    databaseEndpoint = 'mysql://root:changeme@127.0.0.1:3306/mydb'

    app.config['SQLALCHEMY_DATABASE_URI'] = databaseEndpoint
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['TESTING'] = False

    api.init_app(app)
    cors.init_app(app)
    db.init_app(app)


    with app.app_context():
        db.create_all()
        
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)