from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ


def init_flask_app():
    app = Flask(__name__)
    SECRET_KEY = environ.get('SECRET_KEY')
    DATABASE_URI = environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = SECRET_KEY
    return app
