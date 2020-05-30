from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.schema import FetchedValue
from flaskr.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    #email = Column(String(120), unique=True)
    password = Column(String(120), unique=True)

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, unique=False)
    created = Column(TIMESTAMP, server_default=FetchedValue(), unique=False)
    title = Column(String(120), unique=False)
    body = Column(String(120), unique=False)

    def __init__(self, title=None, body=None, author_id=None):
        self.title = title
        self.body = body
        self.author_id = author_id

    def __repr__(self):
        return '<Post %r>' % (self.title)
