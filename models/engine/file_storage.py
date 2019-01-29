#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of instances belonging to a specific instance

        Args:
            cls: a class name you specify to print all instances of within
                __objects
        Return:
            returns a dictionary of either filtered or unfiltered objects
        """

        if cls is not None:
            filtered_dict = {}
            for cls_name_id, cls_instance in self.__objects.items():
                if cls_name_id.split('.')[0] == cls.__name__:
                    filtered_dict[cls_name_id] = cls_instance
            return filtered_dict
        return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj if it exists within the private class "objects" attribute

        Args:
            obj: an instance of a particular class
        """

        if obj is None:
            return
        for key, value in self.__objects.items():
            if obj is value:
                del self.__objects[key]
                break

    def close(self):
        """
        call reload() method for deserializing the JSON file to objects
        """
        self.reload()
