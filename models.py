from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from jikanpy import Jikan
from datetime import datetime
from pytz import timezone
import settings

app = settings.init_flask_app()
db = SQLAlchemy(app)
jikan = Jikan()
eastern = timezone('US/Eastern')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Anime(db.Model):
    __tablename__ = 'anime'
    id = db.Column(db.Integer, primary_key=True)
    english_title = db.Column(db.String())
    num_eps = db.Column(db.Integer)
    year = db.Column(db.Integer)
    image = db.Column(db.String())

    def __init__(self, id, english_title, num_eps, year, image):
        self.id = id
        self.english_title = english_title
        self.num_eps = num_eps
        self.year = year
        self.image = image


"""
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    recip_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    time_sent = db.Column(db.DateTime(), default=datetime.now(eastern))

    def __init__(self, user_id, recip_id, text):
        self.user_id = user_id
        self.recip_id = recip_id
        self.text = text
"""


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False, primary_key=True)
    title = db.Column(db.String())
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=False)
    time_sent = db.Column(db.DateTime(), default=datetime.now(eastern))

    def __init__(self, id, user_id, title, text, image):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.text = text
        self.image = image

"""
class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mime_type = db.Column(db.Text, nullable=False)

    def __init__(self, id, img, name, mime_type):
        self.id = id
        self.img = img
        self.name = name
        self.mime_type = mime_type
"""


db.create_all()
