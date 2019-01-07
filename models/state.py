#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="states")

    @property
    def cities(self):
        city_instances = []
        for cls_name_id, cls_instance in FileStorage.__objects.items():
            class_name_id_list = cls_name_id.split('.')
            if class_name_id_list[0] == "State"\
                    and class_name_id_list[1] == City.state_id:
                city_instances.append(cls_instance)

        return city_instances
