#!/usr/bin/python3
""" new engine DBStorage """
import sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
    """ initialize DBStorage """
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),\
                pool_pre_ping=True)

        if HBNB_ENV == 'test':
            .drop_all() # can't find examples of using drop_all?

    def all(self, cls=None):
    """ query on the current database session
    all objects depending of the class name
    """
    
    def new(self, obj):

    def save(self):

    def delete(self, obj=None):

    def reload(self): 

