#!/usr/bin/python3
# script that deletes all State objects with a name containing the letter a

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in session.query(State).filter(State.name.like('%a%')):
        session.delete(item)

    session.commit()
    session.close()
