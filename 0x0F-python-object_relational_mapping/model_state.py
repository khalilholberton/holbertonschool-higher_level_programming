#!/usr/bin/python3
'''
    contain class State
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
        class State : create a table with the name states with 2 column id, name
    '''
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
