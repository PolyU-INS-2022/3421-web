from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Time

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


class Forum(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    views = Column(Integer, default=0)
    topic = Column(String(255), nullable=False)
    categories = Column(String(255), nullable=False)
    content = Column(String(500))
    created_at = Column(Time, nullable=False)
    creator = Column(Integer, ForeignKey(User.id), nullable=False)
