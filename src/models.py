import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import DateTime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime)
    
    #Agregando relaciones
    favorites = relationship('Favorite', back_populates='user')

    #Metodo para llamar al usuario en el log
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    
class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(10))
    eye_color = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    height = Column(String(10))
    homeworld = Column(String(250))
    mass = Column(String(10))
    skin_color = Column(String(50))
    created = Column(DateTime)
    edited = Column(DateTime)
    
    #Agregando relaciones
    favorited_by = relationship('Favorite', back_populates='character')

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    diameter = Column(String(10))
    gravity = Column(String(10))
    orbital_period = Column(String(10))
    population = Column(String(10))
    rotation_period = Column(String(10))
    surface_water = Column(String(10))
    terrain = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)
    
    #Agregando relaciones
    favorited_by = relationship('Favorite', back_populates='planet')

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    # Define relationships to user, character, and planet
    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorited_by')
    planet = relationship('Planet', back_populates='favorited_by')
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
