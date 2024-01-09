import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

folower = Table('folower', Base.metadata,
    Column('folower_id', Integer, ForeignKey('user.id')),
    Column('to_folower_id', Integer, ForeignKey('user.id')))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True )
    name = Column(String(250))
    lastname= Column(String(250))
    user_name= Column(String(250))
    email=Column(String(250),  unique=True, nullable=False )
    password= Column(String(250))
    followers = relationship(
        'Usuario', 
        secondary=folower,
        primaryjoin=(folower.c.folower_id == id),
        secondaryjoin=(folower.c.to_folower_id == id),
        backref='folower'
    )
    
class Post(Base):
    __tablename__ = 'post'
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Media(Base):
    __tablename__ = 'media'
    Media_id = Column(Integer, primary_key=True )
    post_id = Column(Integer, ForeignKey('post.id') )
    type_media= Column(Enum)
    source_media= Column(String)
    post = relationship(Post)


class Comment(Base):
    __tablename__ = 'comment'
    id_comments =  Column(Integer, primary_key=True )
    comment_text = Column(String)
    author_id = Column(String, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)










#class Person(Base):
   # __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
   # name = Column(String(250), nullable=False)

#class Address(Base):
   # __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
   # id = Column(Integer, primary_key=True)
   # street_name = Column(String(250))
   # street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
