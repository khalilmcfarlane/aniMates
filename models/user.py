from enum import unique
import flask
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self,password = password
 
