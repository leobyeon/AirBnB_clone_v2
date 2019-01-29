#!/usr/bin/python3
""" new engine DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ initialize DBStorage """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                user, pwd, host, db), pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query on the current database session
        all objects depending of the class name
        """
        filtered_dict = {}
        if cls is None:
            for table in [City, State, User, Place, Amenity, Review]:
                for instance in self.__session.query(table).all():
                    filtered_dict["{}.{}".format(
                       table, instance.id)] = instance

        else:
            for instance in self.__session.query(eval(cls)).all():
                filtered_dict["{}.{}".format(
                    eval(cls).__name__, instance.id)] = instance

        return filtered_dict

    def new(self, obj):
        """ Adds obj to the current session

            Args:
                obj: the instance to be added

        """
        self.__session.add(obj)

    def save(self):
        """ saves changes made to the session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes an object from the current session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ recreates a session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)

    def close(self):
        """
        call remove() method on the private session
        """
        self.__session.close()
