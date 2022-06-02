from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import settings

app = settings.init_flask_app()
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self,password = password
 
