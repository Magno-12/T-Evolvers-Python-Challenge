import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from event.metrics.views import catalog
app.register_blueprint(catalog)

db.create_all()