from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date, DateTime
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Image(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255), nullable=False)
    path = Column(String(255), nullable=False)


class Memorial(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    deceasedName = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    death_date = Column(Date, nullable=False)
    epitaph = Column(String(255), nullable=True)
    memorialDescription = Column(String(255), nullable=True)
    user = Column("user", ForeignKey(User.id), nullable=False)
    image = Column("image", ForeignKey(Image.id), nullable=False)


class Message(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    content = Column(String(500))
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    creator = Column("creator", ForeignKey(User.id), nullable=False)