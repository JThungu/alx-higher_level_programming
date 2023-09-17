#!/usr/bin/python3
"""
state model that contain the class definition
 of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Represents a State entity linked to the 'states' table in MySQL.

    Attributes:
        id (Column): An auto-generated, unique integer primary key, cannot be null.
        name (Column): A string with a maximum length of 128 characters, cannot be null.

    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
