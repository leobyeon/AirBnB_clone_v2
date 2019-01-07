#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """Class definition for City, inherits from BaseModel and Base

    Class Attributes:
        Private:
            tablename: the table that is mapped to the class

        Public:
            state_id: Foreign key that maps to states.id
            name: the name of the city that the user puts in
    """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
