#!/usr/bin/python3
""" new engine DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base


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
            for instance in self.__session.query(
                    User, State, City, Amenity, Place, Review).all():
                filtered_dict["{}.{}".format(
                    instance.name, instance.id)] = instance

        else:
            for instance in self.__session.query(cls).all():
                filtered_dict["{}.{}".format(
                    instance.name, instance.id)] = instance

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
        self.__session = Session()
