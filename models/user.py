from sqlalchemy import *
from extentions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usename = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.string)