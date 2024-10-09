from sqlalchemy import *
from extentions import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    phone = Column(String, nullable=False, index=True)