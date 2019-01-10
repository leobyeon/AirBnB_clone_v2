#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
import os
import models
from sqlalchemy.orm import relationship
from models.amenity import Amenity


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id', String(60), ForeignKey("places.id"),
            primary_key=True, nullable=False),
        Column(
            'amenity_id', String(60), ForeignKey("amenities.id"),
            primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    metadata = Base.metadata

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        amenities = relationship(
                "Amenity", secondary=place_amenity,
                backref="place_amenities", viewonly=False)
        reviews = relationship("Review", cascade="delete", backref="place")
    else:
        amenities = ""
        reviews = ""

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    @property
    def amenities(self):
        """ gets the list of amenities """
        a_ls = []
        a_objs = models.storage.all(Amenity)
        for obj_key, obj_val in a_objs.items():
            if obj_val.id in self.amenity_ids:
                a_ls.append(obj)
        return a_ls

    @amenities.setter
    def amenities(self, obj):
        """ handles append method for amenities """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)

    @property
    def reviews(self):
        """
        getter attribute 'reviews' that returns a list of Review
        instances with place_id equal to Place.id
        """
        rev_objs = models.storage.all("Review")
        place_objs = models.storage.all("Place")
        rev_ls = []
        for name_id, value in rev_objs.items():
            for pls_name_id in place_objs.keys():
                if value.place_id == pls_name_id.split('.')[1]:
                    rev_ls.append(value)
        return rev_ls