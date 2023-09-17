#!/usr/bin/python3
"""
State model containing the class definition
 of a City and an instance Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Inherits from Base and represents a City entity linked to the 'cities' table in MySQL.

    Attributes:
        id (Column): An auto-generated, unique integer primary key.
        name (Column): A string of up to 128 characters, cannot be null.
        state_id (Column): An integer representing a foreign key to the 'states.id' column, cannot be null.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
