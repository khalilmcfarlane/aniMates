from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import settings

app = settings.init_flask_app()
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer)
    username = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30), primary_key=True)


    def __init__(self, username, password):
        self.username = username
        self.password = password
        
db.create_all()
 
