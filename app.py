from flask import Flask
from db import db
from flask_cors import CORS
from api import api
from config.extensions import jwt
from datetime import timedelta
import pprint
import pymysql

pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

cors = CORS()


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = env['wsgi.errors']
        pprint.pprint(('REQUEST', env), stream=errorlog)

        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(env, log_response)

def create_app():
    app = Flask(__name__)
    
    #databaseEndpoint = 'mysql://root:changeme@127.0.0.1:3306/mydb'
    databaseEndpoint = 'sqlite:///data.db'

    app.config['SQLALCHEMY_DATABASE_URI'] = databaseEndpoint
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['TESTING'] = False
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours = 12)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days = 30)
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

    api.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    return app

if __name__ == "__main__":
    app = create_app()
    # app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    app.run(debug = True)