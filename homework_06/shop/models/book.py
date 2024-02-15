from sqlalchemy import Column, String
from .database import db


class Book(db.Model):
    name = Column(String, nullable=False)