#!/usr/bin/python3
""" new engine DBStorage """
import sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


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

        if env == 'test':
            .drop_all() # can't find examples of using drop_all?

    def all(self, cls=None):
    """ query on the current database session
    all objects depending of the class name
    """
    
    def new(self, obj):

    def save(self):

    def delete(self, obj=None):

    def reload(self): 

