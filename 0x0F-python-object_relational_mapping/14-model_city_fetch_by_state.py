#!/usr/bin/python3
# prints all City objects from the database hbtn_0e_14_usa:

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({:d}) {}".format(item.State.name,
                                     item.City.id,
                                     item.City.name))
    session.close()
